import socket, pickle, threading, time
import tkinter as tk
from prop_class_for_online_version import my_property_class
from player_class_online_version import Player

# importing the choosecolor package
from tkinter import colorchooser

client = socket.socket()
client.connect(("192.168.29.201",9999))
HEADER = 10
container = tk.Tk()

# setting width and height of tkinter window so as to fit screen!
width = container.winfo_screenwidth()  # width of screen
height = container.winfo_screenheight()  # height of screen
container.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

# intro page of the game where one can join or create room, select their favourite color for the game
start_frame= tk.Frame(container, width=width, height=height)
start_frame.grid(row=0, column=0, sticky="nsew")

# make a grid on the container so as to make placing easier- you can ignore this just gui stuff
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=0)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=1)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=2)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=3)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=4)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=5)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=6)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=7)

font = ("Courier", 14)

two_btns_label = tk.Label(start_frame, text = "What do you want to do?",font=font)
two_btns_label.grid(row=2,column=2, columnspan=3)
# give our client a choice of creating or joining a room
create_room_btn = tk.Button(start_frame,text="Create Room",command=lambda:create_room())
create_room_btn.grid(row=3,column=2)
join_room_btn = tk.Button(start_frame, text="Join Room", command=lambda: join_room())
join_room_btn.grid(row=3, column=4)

def create_room():
    global player_desig
    player_desig = "host"
    two_btns_label.grid_forget()
    join_room_btn.grid_forget()
    create_room_btn.grid_forget()
    print("sending to create new room!")
    client.send(bytes("create room", 'utf-8'))
    ask_username()

def join_room():
    global player_desig
    player_desig = "player"
    two_btns_label.grid_forget()
    join_room_btn.grid_forget()
    create_room_btn.grid_forget()
    print("sending to join room!")
    client.send(bytes("join room", 'utf-8'))
    ask_room_num()

def ask_username():
    # ask for username
    global ok_but_for_username, username_entry, username_label
    username_label = tk.Label(start_frame, text="Enter your username", font=font)
    username_label.grid(row=2, column=3)
    username_entry = tk.Entry(start_frame)
    ok_but_for_username = tk.Button(start_frame, text="Okay", font=font, command=lambda: ok_but_for_username_clicked())
    username_entry.grid(row=3, column=3)
    ok_but_for_username.grid(row=4, column=3)

def ok_but_for_username_clicked():
    username_label.grid_forget()
    ok_but_for_username.grid_forget()
    username_entry.grid_forget()
    global username
    username = str(username_entry.get())
    print("sending username")
    username_sendable = f"{len(username):<{HEADER}}" + username
    client.send(bytes(username_sendable, 'utf-8'))
    check_on_new_thread_npl = recv_new_players_list_thread()
    check_on_new_thread_npl.start()
    print("check for new players list",check_on_new_thread_npl.native_id)

def ask_room_num():
    global room_num_entry, ok_but_room_num, room_label
    room_label = tk.Label(start_frame,text="Enter the number of the room which you want to join!", font=font)
    room_label.grid(row=2, column=2, columnspan=3)
    room_num_entry = tk.Entry(start_frame)
    room_num_entry.grid(row=3,column=3)
    ok_but_room_num = tk.Button(start_frame, text="Ok",command = lambda:ok_but_room_num_clkd())
    ok_but_room_num.grid(row=4,column=3)

def ok_but_room_num_clkd():
    room_label.grid_forget()
    room_num_entry.grid_forget()
    ok_but_room_num.grid_forget()
    room = room_num_entry.get()
    client.send(bytes(room,'utf-8'))
    status = client.recv(1024).decode('utf-8')

    if str(status) == "error":
        # for now only
        quit()

    if str(status) == "joined successfully":
        # ask and then send the username
        # ask for username
        ask_username()

    if str(status) == "room doesn't exist":
        # ask client to enter a valid room no.
        print(str(status))
        ask_room_num()

    if str(status) == "unable to join temp":
        # ask client to wait for some time and then try to join again (this is the most rare to happen)
        print("please try to join the room in a few seconds")
        ask_room_num()

    if str(status) == "room locked":
        # ask client to enter another room num
        print("room is either full or locked by the host!")
        ask_room_num()

class recv_new_players_list_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("for thread recv new players list")
        # accept new players list as new players do join and the list needs to be updated
        global check_for_new_players_list_stat, start_game_btn, player_desig
        start_btn_shown = False
        print("checking for new players list on",threading.Thread.getName(self))

        while True:
            new_players_list = client.recv(1024)
            if new_players_list:
                new_players_list = pickle.loads(new_players_list)

                if new_players_list == "start game":
                    print("recved start game",username)
                    break

                else:
                    print("new players list = ", new_players_list)
                    # only display start btn when more than one player is there in the room and also dont show again
                    # if already on grid!
                    if len(new_players_list) > 1 and start_btn_shown == False and player_desig == "host":
                        start_game_btn = tk.Button(start_frame, text="Start Game",command=lambda: start_game_host())
                        start_game_btn.grid(row=4, column=3)
                        start_btn_shown = True

                    # incase a player joins and then leaves
                    if len(new_players_list) == 1 and start_btn_shown == True:
                        start_game_btn.grid_forget()
                        start_btn_shown = False

        recv_details_thread = threading.Thread(target=recv_game_details)
        recv_details_thread.start()
        print("recv game setails thread:",recv_details_thread.native_id)

def start_game_host():
    start_game_btn.grid_forget()
    client.send(bytes("start the game",'utf-8'))
    print("player started the game")

def recv_game_details():
    global data_holder
    print(threading.enumerate())
    print("recving game info")
    data_holder = client.recv(1024)
    data_holder = pickle.loads(data_holder)
    print(data_holder)

    display_thread = threading.Thread(target= display_game_screen())
    display_thread.start()
    cc_thread = threading.Thread(target= choose_color())
    cc_thread.start()

def choose_color():

    # GIVE DEFAULT COLOR
    print(threading.enumerate())
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    print(color_code)
    scr = (username, color_code[1])
    # send our server the color our client chose
    client.send(pickle.dumps(scr))
    get_color_updates()

def get_color_updates():
    global created_objs
    created_objs = {}
    client.send(pickle.dumps("start"))
    while True:
        npc = pickle.loads(client.recv(1024))
        print(npc)

        if npc == "end":
            break
        data_holder["game info"][npc[0]]["color"] = npc[1]
        print(data_holder)
        created_objs.update({npc[0]:Player(main_frame,status_frame,data_holder,npc[0])})
        print('object created:',npc[0])

def recv_data_updates():
    while True:
        data_update = pickle.loads(client.recv(1024))
        print(data_update)
        if len(data_update) == 3:
            data_holder[[data_update[0]]][[data_update[1]]] = data_update[2]
        elif len(data_update) == 2:
            data_holder[[data_update[0]]] = data_update[1]
        print(data_holder)
        # run update info method here

def seek_chance():
    while True:
        time.sleep(1.0)
        if data_holder["chance"] == data_holder["player chances"][username]:
            pass
            # display roll dice and other stuff like that
        else:
            time.sleep(1.0)



def display_game_screen():
    start_frame.grid_forget()
    global main_frame, status_frame, width, height
    main_frame = tk.Frame(container)

    main_frame.grid(row=0, column=0, sticky="nsew")
    width = main_frame.winfo_screenwidth()  # width of screen
    height = main_frame.winfo_screenheight()  # height of screen
    width -= 325
    height -= 345
    width = width / 9
    height = height / 9

    # top lane

    free_parking = my_property_class(main_frame,"Free Parking", 0, 0, 160, 140)
    free_parking.update_dicto(free_parking, 20)

    strand = my_property_class(main_frame,"Strand", 0, 1, width, 140, "firebrick1", 18, 220,
                               90, 250, 700, 875, 1050, 150, 150, 110, "s")
    strand.update_dicto(strand, 21)

    chance2 = my_property_class(main_frame,"Chance", 0, 2, width, 140)
    chance2.update_dicto(chance2, 22)

    fleet_street = my_property_class(main_frame,"fleet street", 0, 3, width, 140, "firebrick1", 18, 220,
                                     90, 250, 700, 875, 1050, 150, 150, 110, "s")
    fleet_street.update_dicto(fleet_street, 23)

    trafalagar_square = my_property_class(main_frame,"trafalagar square", 0, 4, width, 140, "firebrick1", 20, 240,
                                          100, 300, 750, 925, 1100, 150, 150, 120, "s")
    trafalagar_square.update_dicto(trafalagar_square, 24)

    fenchurch_st_station = my_property_class(main_frame,"fenchurch st station", 0, 5, width, 140)
    fenchurch_st_station.update_dicto(fenchurch_st_station, 25)

    licester_square = my_property_class(main_frame,"licester square", 0, 6, width, 140, "yellow", 22, 290,
                                        110, 330, 800, 975, 1150, 150, 150, 130, "s")
    licester_square.update_dicto(licester_square, 26)

    coventry_street = my_property_class(main_frame,"coventry street", 0, 7, width, 140, "yellow", 22, 290,
                                        110, 330, 800, 975, 1150, 150, 150, 130, "s")
    coventry_street.update_dicto(coventry_street, 27)

    water_works = my_property_class(main_frame,"water works", 0, 8, width, 140)
    water_works.update_dicto(water_works, 28)

    piccadilly = my_property_class(main_frame,"piccadilly", 0, 9, width, 140, "yellow", 24, 280,
                                   120, 360, 850, 1025, 1200, 150, 150, 140, "s")
    piccadilly.update_dicto(piccadilly, 29)

    go_to_jail = my_property_class(main_frame,"go_to_jail", 0, 10, 160, 140)
    go_to_jail.update_dicto(go_to_jail, 30)

    # right lane
    regent_street = my_property_class(main_frame,"regent street", 1, 10, 160, height, "green", 26, 300,
                                      130, 390, 900, 1100, 1275, 200, 200, 150, "w")
    regent_street.update_dicto(regent_street, 31)

    oxford_street = my_property_class(main_frame,"oxford street", 2, 10, 160, height, "green", 26, 300,
                                      130, 390, 900, 1100, 1275, 200, 200, 150, "w")
    oxford_street.update_dicto(free_parking, 32)

    community_chest = my_property_class(main_frame,"community_chest", 3, 10, 160, height)
    community_chest.update_dicto(community_chest, 33)

    bond_street = my_property_class(main_frame,"bond street", 4, 10, 160, height, "green", 28, 320,
                                    150, 450, 1000, 1200, 1400, 200, 200, 160, "w")
    bond_street.update_dicto(bond_street, 34)

    liverpool_st_station = my_property_class(main_frame,"liverpool_st_station", 5, 10, 160, height)
    liverpool_st_station.update_dicto(liverpool_st_station, 35)

    chance3 = my_property_class(main_frame,"chance3", 6, 10, 160, height)
    chance3.update_dicto(chance3, 36)

    park_lane = my_property_class(main_frame,"park_lane", 7, 10, 160, height, "dark blue", 35, 350,
                                  175, 500, 1100, 1300, 1500, 200, 200, 175, "w")
    park_lane.update_dicto(park_lane, 37)

    super_tax = my_property_class(main_frame,"super_tax", 8, 10, 160, height)
    super_tax.update_dicto(super_tax, 38)

    mayfair = my_property_class(main_frame,"mayfair", 9, 10, 160, height, "dark blue", 50, 400,
                                200, 600, 1400, 1700, 2000, 200, 200, 200, "w")
    mayfair.update_dicto(mayfair, 39)

    # lower lane

    just_visiting = my_property_class(main_frame,"just_visting", 10, 0, 160, 140)
    just_visiting.update_dicto(just_visiting, 10)

    pentoville_road = my_property_class(main_frame,"pentoville road", 10, 1, width, 140, "light blue", 8, 120,
                                        40, 100, 300, 450, 600, 50, 50, 60, "n")
    pentoville_road.update_dicto(pentoville_road, 9)

    euston_road = my_property_class(main_frame,"euston road", 10, 2, width, 140, "light blue", 6, 100,
                                    30, 90, 270, 400, 550, 50, 50, 50, "n")
    euston_road.update_dicto(euston_road, 8)

    chance1 = my_property_class(main_frame,"chance", 10, 3, width, 140)
    chance1.update_dicto(chance1, 7)

    the_angel_islington = my_property_class(main_frame,"the angel islington", 10, 4, width, 140, "light blue", 6, 100,
                                            30, 90, 270, 400, 550, 50, 50, 50, "n")
    the_angel_islington.update_dicto(the_angel_islington, 6)

    kings_cross_station = my_property_class(main_frame,"kings cross station", 10, 5, width, 140)
    kings_cross_station.update_dicto(kings_cross_station, 5)

    income_tax = my_property_class(main_frame,"income tax!", 10, 6, width, 140)
    income_tax.update_dicto(income_tax, 4)

    white_chapal_road = my_property_class(main_frame,"white chapal road", 10, 7, width, 140, "brown", 4, 60,
                                          20, 60, 180, 320, 450, 50, 50, 30, "n")
    white_chapal_road.update_dicto(white_chapal_road, 3)

    community_chest1 = my_property_class(main_frame,"community chest", 10, 8, width, 140)
    community_chest1.update_dicto(community_chest1, 2)

    old_kent_road = my_property_class(main_frame,"old kent road", 10, 9, width, 140, "brown", 2, 60,
                                      10, 30, 90, 160, 250, 50, 50, 30, "n")
    old_kent_road.update_dicto(old_kent_road, 1)

    go_box = my_property_class(main_frame,"go box", 10, 10, 160, 140)
    go_box.update_dicto(go_box, 0)

    # left lane

    pall_mall = my_property_class(main_frame,"pall mall", 9, 0, 160, height, "pink", 10, 140,
                                  50, 150, 450, 625, 750, 100, 50 * 2, 70, "e")
    pall_mall.update_dicto(pall_mall, 11)

    electric_company = my_property_class(main_frame,"electric company", 8, 0, 160, height)
    electric_company.update_dicto(electric_company, 12)

    white_hall = my_property_class(main_frame,"white hall", 7, 0, 160, height, "pink", 10, 140,
                                   50, 150, 450, 625, 750, 100, 50 * 2, 70, "e")
    white_hall.update_dicto(white_hall, 13)

    northumber_ld_avenue = my_property_class(main_frame,"northumberl'd avenue", 6, 0, 160, height, "pink", 12, 160, 60,
                                             180, 500, 700, 900, 100, 100, 80, "e")
    northumber_ld_avenue.update_dicto(northumber_ld_avenue, 14)

    marylebone_station = my_property_class(main_frame,"marltbone station", 5, 0, 160, height)
    marylebone_station.update_dicto(marylebone_station, 15)

    bow_street = my_property_class(main_frame,"bow street", 4, 0, 160, height, "orange", 14, 180,
                                   70, 200, 550, 750, 950, 100, 50 * 2, 90, "e")
    bow_street.update_dicto(bow_street, 16)

    community_chest2 = my_property_class(main_frame,"community chest", 3, 0, 160, height)
    community_chest2.update_dicto(community_chest2, 17)

    marlborough_street = my_property_class(main_frame,"marlborough street", 2, 0, 160, height, "orange", 14, 180,
                                           70, 200, 550, 750, 950, 100, 50 * 2, 90, "e")
    marlborough_street.update_dicto(marlborough_street, 18)

    vine_street = my_property_class(main_frame,"vine street", 1, 0, 160, height, "orange", 16, 200,
                                    80, 220, 600, 800, 1000, 100, 50 * 2, 100, "e")
    vine_street.update_dicto(vine_street, 19)

    monopoly_dis = tk.Label(main_frame, text="Monopoly", bg="tomato1", fg="white")
    monopoly_dis.grid(row=5, column=5)

    sf_width = 8 * width + 2
    sf_height = 3 * height
    status_frame = tk.LabelFrame(main_frame, text="Status Box", bg="light green", fg="black",
                                 highlightbackground="black", highlightthickness=1, width=sf_width,height=sf_height)
    status_frame.grid(rowspan=4, columnspan=9, row=1, column=1)

#def make_player_class_objs():


# ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
"""    color_button = tk.Button(start_frame, text="Select color",
                    command=lambda:choose_color())
    color_button.grid()"""
container.mainloop()