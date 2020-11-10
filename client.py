import random
import socket, pickle, threading, time
import tkinter as tk
from prop_class_for_online_version import my_property_class
from player_class_online_version import Player

# importing the choosecolor package
from tkinter import colorchooser, ttk

client = socket.socket()
client.connect(("192.168.29.202", 9999))

container = tk.Tk()

# setting width and height of tkinter window so as to fit screen!
width = container.winfo_screenwidth()  # width of screen
height = container.winfo_screenheight()  # height of screen
container.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

# intro page of the game where one can join or create room, select their favourite color for the game
start_frame = tk.Frame(container, width=width, height=height)
start_frame.grid(row=0, column=0, sticky="nsew")

# make a grid on the container so as to make placing easier- you can ignore this just gui stuff
tk.Frame(start_frame, width=width / 7, height=height / 7).grid(row=0, column=0)
tk.Frame(start_frame, width=width / 7, height=height / 7).grid(row=0, column=1)
tk.Frame(start_frame, width=width / 7, height=height / 7).grid(row=0, column=2)
tk.Frame(start_frame, width=width / 7, height=height / 7).grid(row=0, column=3)
tk.Frame(start_frame, width=width / 7, height=height / 7).grid(row=0, column=4)
tk.Frame(start_frame, width=width / 7, height=height / 7).grid(row=0, column=5)
tk.Frame(start_frame, width=width / 7, height=height / 7).grid(row=0, column=6)
tk.Frame(start_frame, width=width / 7, height=height / 7).grid(row=0, column=7)

font = ("Courier", 14)

two_btns_label = tk.Label(start_frame, text="What do you want to do?", font=font)
two_btns_label.grid(row=2, column=2, columnspan=3)
# give our client a choice of creating or joining a room
create_room_btn = tk.Button(start_frame, text="Create Room", command=lambda: create_room())
create_room_btn.grid(row=3, column=2)
join_room_btn = tk.Button(start_frame, text="Join Room", command=lambda: join_room())
join_room_btn.grid(row=3, column=4)


def create_room():
    global player_desig
    player_desig = "host"
    two_btns_label.grid_forget()
    join_room_btn.grid_forget()
    create_room_btn.grid_forget()
    print("sending to create new room!")
    client.send(pickle.dumps("create room"))
    ask_username()


def join_room():
    global player_desig
    player_desig = "player"
    two_btns_label.grid_forget()
    join_room_btn.grid_forget()
    create_room_btn.grid_forget()
    print("sending to join room!")
    client.send(pickle.dumps("join room"))
    ask_room_num()


def ask_room_num():
    global room_num_entry, ok_but_room_num, room_label, room_num_display_frame
    room_num_display_frame = tk.Frame(container)
    room_num_display_frame.grid()

    recv_rooms_list_thread_OBJECT = recv_rooms_list_thread()
    recv_rooms_list_thread_OBJECT.start()

    room_label = tk.Label(start_frame, text="Enter the number of the room which you want to join!", font=font)
    room_label.grid(row=2, column=2, columnspan=3)
    ok_but_room_num = tk.Button(start_frame, text="Okay", font=font, command=lambda: ok_but_room_num_clkd())
    ok_but_room_num.grid(row=4, column=3)


class recv_rooms_list_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        # display a list of players on the screen
        # it would be in the form of a treeview (of ttk)

        # define our treeview

        global rooms_view
        rooms_view = ttk.Treeview(room_num_display_frame, selectmode="browse")

        # format our columns
        rooms_view["columns"] = ("Room Number", "Host Name", "No. of Players")
        rooms_view.column("#0", width=0)
        rooms_view.column("Room Number", width=150, minwidth=50, anchor="w")
        rooms_view.column("Host Name", width=150, minwidth=40, anchor="w")
        rooms_view.column("No. of Players", width=100, minwidth=20, anchor="w")

        # create headings
        rooms_view.heading("#0", text="")
        rooms_view.heading("Room Number", text="Room Number", anchor="w")
        rooms_view.heading("Host Name", text="Host Name", anchor="w")
        rooms_view.heading("No. of Players", text="No. of Players", anchor="w")

        # pack to the screen
        rooms_view.pack()

        # we will add data as and when we recv stuff

        print("checking for new players list on", threading.Thread.getName(self))

        # list of players we have taken note of
        noted_rooms = []
        # contains the n_players of all room nums recved so as later we can change the display when n-players change
        noted_n_players = {}

        stringvars = {}
        global rooms_list
        stat_list = ["error", "joined successfully", "room doesn't exist", "room locked"]

        while True:
            time.sleep(0.5)
            print("recving rooms list")

            rooms_list = pickle.loads(client.recv(1024))

            print("new rooms list = ", rooms_list)

            if rooms_list in stat_list:
                analyze_stat(rooms_list)
                break
            else:
                for room in rooms_list:

                    if room[0] not in noted_rooms:

                        stringvars.update({room[0]: tk.StringVar()})
                        stringvars[room[0]].set(str(room[2]))
                        # add data for the player in treeview

                        rooms_view.insert(parent="", index="end", text="",
                                          values=(room[0], room[1], stringvars[room[0]].get()))

                        # add the player in noted players so we do not double display the player
                        noted_rooms.append(room[0])
                        # add n_players with corresponding room num
                        noted_n_players.update({room[0]: room[2]})

                    else:
                        # this means we have noted the room already, so just check if we need to update all no. of
                        #  players in the display
                        if noted_n_players[room[0]] != room[2]:
                            # so this code will run when we recved a new num for no. of players
                            # update display
                            stringvars[room[0]].set(room[2])

                        else:
                            # means nothing to change
                            # this is not possible as we only send data when we have a change
                            print("There is a problem, no data change but recved new rooms list")


def ok_but_room_num_clkd():
    try:
        ok_but_room_num.grid_forget()
        room_num_display_frame.grid_forget()
        room_label.grid_forget()

        s = rooms_view.selection()[0]
        selected = rooms_view.focus()
        room = rooms_view.item(selected, "values")
        room = room[0]
        print(room)
        client.send(pickle.dumps(room))

    except IndexError:
        print("None selected")


def analyze_stat(status):
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
    global username
    username_label.grid_forget()
    ok_but_for_username.grid_forget()
    username_entry.grid_forget()

    username = username_entry.get()

    username = str(username)
    client.send(pickle.dumps(username))
    response = pickle.loads(client.recv(1024))
    print(response)
    if response == "occupied username":
        ask_username()
    else:
        container.title(username)
        check_on_new_thread_npl = recv_new_players_list_thread()
        check_on_new_thread_npl.start()


class recv_new_players_list_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # display a list of players on the screen
        # it would be in the form of a treeview (of ttk)

        # define our treeview

        global people_view
        people_view = ttk.Treeview(container, selectmode="none")

        # format our columns
        people_view["columns"] = ("Name", "Designation", "Chance")
        people_view.column("#0", width=0)
        people_view.column("Name", width=150, minwidth=50, anchor="w")
        people_view.column("Designation", width=150, minwidth=40, anchor="w")
        people_view.column("Chance", width=100, minwidth=20, anchor="w")

        # create headings
        people_view.heading("#0", text="")
        people_view.heading("Name", text="Player Name", anchor="w")
        people_view.heading("Designation", text="Designation", anchor="w")
        people_view.heading("Chance", text="Chance", anchor="w")

        # pack to the screen
        people_view.grid()

        # we will add data as and when we recv stuff

        # accept new players list as new players do join and the list needs to be updated

        global check_for_new_players_list_stat, start_game_btn, player_desig

        start_btn_shown = False
        print("checking for new players list on", threading.Thread.getName(self))

        # list of players we have taken note of
        noted_players = []

        while True:
            time.sleep(1)
            new_players_list = client.recv(1024)
            if new_players_list:
                new_players_list = pickle.loads(new_players_list)
                print("npl = ", new_players_list)

                if new_players_list == "start game":
                    print("recved start game", username)
                    break

                else:
                    print("new players list = ", new_players_list)
                    # only display start btn when more than one player is there in the room and also dont show again
                    # if already on grid!
                    if len(new_players_list) > 1 and start_btn_shown == False and player_desig == "host":
                        start_game_btn = tk.Button(start_frame, text="Start Game", command=lambda: start_game_host())
                        start_game_btn.grid(row=2, column=1)
                        start_btn_shown = True

                    # incase a player joins and then leaves
                    if len(new_players_list) == 1 and start_btn_shown == True:
                        start_game_btn.grid_forget()
                        start_btn_shown = False

                    for player in new_players_list:
                        if player not in noted_players:

                            # if player index in the list is zero it means he is a host
                            if new_players_list[0] == player:
                                desig = "Host"

                            else:
                                desig = "Player"

                            # add data for the player in treeview
                            # new_players_list.index(player) returns the index of the item in the list
                            people_view.insert(parent="", index="end", text="",
                                               values=(player, desig, new_players_list.index(player) + 1))

                            # add the player in noted players so we do not double display the player
                            noted_players.append(player)

                        else:
                            pass
            time.sleep(1)
        recv_details_thread = threading.Thread(target=recv_game_details)
        recv_details_thread.start()


def start_game_host():
    start_game_btn.grid_forget()
    client.send(pickle.dumps("start the game"))
    print("player started the game")


def recv_game_details():
    global data_holder
    print(threading.enumerate())
    print("recving game info")
    data_holder = pickle.loads(client.recv(2048))
    print("\n", data_holder, "\n")
    display_thread = threading.Thread(target=display_game_screen())
    display_thread.start()
    cc_thread = threading.Thread(target=choose_color())
    cc_thread.start()


def choose_color():
    # this blocks the execution of all the threads so a work around is made , u will see later

    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    print("color code = ", color_code)
    if color_code[1] is None:
        choose_color()
    else:
        # scr = sendable color tuple
        scr = (username, color_code[1])
        # send our server the color our client chose
        client.send(pickle.dumps(scr))
        get_color_updates()


def get_color_updates():
    global created_objs
    created_objs = {}
    created_objs_list = []
    print(threading.enumerate())

    while True:

        print("still running")
        npc = pickle.loads(client.recv(1024))
        print("npc =", npc)

        data_holder["game info"][npc[0]]["color"] = npc[1]
        created_objs.update({npc[0]: Player(main_frame, status_frame, data_holder, npc[0])})
        created_objs_list.append(npc)
        print('object created:', npc[0])
        print(len(created_objs_list), len(data_holder["players list"]))
        print("checking for breaking loop")
        if len(created_objs_list) == len(data_holder["players list"]):
            print("breaking while loop")
            final_stage_tweaks()
            break

    print("while true ended")


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

    free_parking = my_property_class(main_frame, "Free Parking", 0, 0, 160, 140)
    free_parking.update_dicto(free_parking, 20)

    strand = my_property_class(main_frame, "Strand", 0, 1, width, 140, "firebrick1", 18, 220,
                               90, 250, 700, 875, 1050, 150, 150, 110, "s")
    strand.update_dicto(strand, 21)

    chance2 = my_property_class(main_frame, "Chance", 0, 2, width, 140)
    chance2.update_dicto(chance2, 22)

    fleet_street = my_property_class(main_frame, "fleet street", 0, 3, width, 140, "firebrick1", 18, 220,
                                     90, 250, 700, 875, 1050, 150, 150, 110, "s")
    fleet_street.update_dicto(fleet_street, 23)

    trafalagar_square = my_property_class(main_frame, "trafalagar square", 0, 4, width, 140, "firebrick1", 20, 240,
                                          100, 300, 750, 925, 1100, 150, 150, 120, "s")
    trafalagar_square.update_dicto(trafalagar_square, 24)

    fenchurch_st_station = my_property_class(main_frame, "fenchurch st station", 0, 5, width, 140)
    fenchurch_st_station.update_dicto(fenchurch_st_station, 25)

    licester_square = my_property_class(main_frame, "licester square", 0, 6, width, 140, "yellow", 22, 290,
                                        110, 330, 800, 975, 1150, 150, 150, 130, "s")
    licester_square.update_dicto(licester_square, 26)

    coventry_street = my_property_class(main_frame, "coventry street", 0, 7, width, 140, "yellow", 22, 290,
                                        110, 330, 800, 975, 1150, 150, 150, 130, "s")
    coventry_street.update_dicto(coventry_street, 27)

    water_works = my_property_class(main_frame, "water works", 0, 8, width, 140)
    water_works.update_dicto(water_works, 28)

    piccadilly = my_property_class(main_frame, "piccadilly", 0, 9, width, 140, "yellow", 24, 280,
                                   120, 360, 850, 1025, 1200, 150, 150, 140, "s")
    piccadilly.update_dicto(piccadilly, 29)

    go_to_jail = my_property_class(main_frame, "go_to_jail", 0, 10, 160, 140)
    go_to_jail.update_dicto(go_to_jail, 30)

    # right lane
    regent_street = my_property_class(main_frame, "regent street", 1, 10, 160, height, "green", 26, 300,
                                      130, 390, 900, 1100, 1275, 200, 200, 150, "w")
    regent_street.update_dicto(regent_street, 31)

    oxford_street = my_property_class(main_frame, "oxford street", 2, 10, 160, height, "green", 26, 300,
                                      130, 390, 900, 1100, 1275, 200, 200, 150, "w")
    oxford_street.update_dicto(free_parking, 32)

    community_chest = my_property_class(main_frame, "community_chest", 3, 10, 160, height)
    community_chest.update_dicto(community_chest, 33)

    bond_street = my_property_class(main_frame, "bond street", 4, 10, 160, height, "green", 28, 320,
                                    150, 450, 1000, 1200, 1400, 200, 200, 160, "w")
    bond_street.update_dicto(bond_street, 34)

    liverpool_st_station = my_property_class(main_frame, "liverpool_st_station", 5, 10, 160, height)
    liverpool_st_station.update_dicto(liverpool_st_station, 35)

    chance3 = my_property_class(main_frame, "chance3", 6, 10, 160, height)
    chance3.update_dicto(chance3, 36)

    park_lane = my_property_class(main_frame, "park_lane", 7, 10, 160, height, "dark blue", 35, 350,
                                  175, 500, 1100, 1300, 1500, 200, 200, 175, "w")
    park_lane.update_dicto(park_lane, 37)

    super_tax = my_property_class(main_frame, "super_tax", 8, 10, 160, height)
    super_tax.update_dicto(super_tax, 38)

    mayfair = my_property_class(main_frame, "mayfair", 9, 10, 160, height, "dark blue", 50, 400,
                                200, 600, 1400, 1700, 2000, 200, 200, 200, "w")
    mayfair.update_dicto(mayfair, 39)

    # lower lane

    just_visiting = my_property_class(main_frame, "just_visting", 10, 0, 160, 140)
    just_visiting.update_dicto(just_visiting, 10)

    pentoville_road = my_property_class(main_frame, "pentoville road", 10, 1, width, 140, "light blue", 8, 120,
                                        40, 100, 300, 450, 600, 50, 50, 60, "n")
    pentoville_road.update_dicto(pentoville_road, 9)

    euston_road = my_property_class(main_frame, "euston road", 10, 2, width, 140, "light blue", 6, 100,
                                    30, 90, 270, 400, 550, 50, 50, 50, "n")
    euston_road.update_dicto(euston_road, 8)

    chance1 = my_property_class(main_frame, "chance", 10, 3, width, 140)
    chance1.update_dicto(chance1, 7)

    the_angel_islington = my_property_class(main_frame, "the angel islington", 10, 4, width, 140, "light blue", 6, 100,
                                            30, 90, 270, 400, 550, 50, 50, 50, "n")
    the_angel_islington.update_dicto(the_angel_islington, 6)

    kings_cross_station = my_property_class(main_frame, "kings cross station", 10, 5, width, 140)
    kings_cross_station.update_dicto(kings_cross_station, 5)

    income_tax = my_property_class(main_frame, "income tax!", 10, 6, width, 140)
    income_tax.update_dicto(income_tax, 4)

    white_chapal_road = my_property_class(main_frame, "white chapal road", 10, 7, width, 140, "brown", 4, 60,
                                          20, 60, 180, 320, 450, 50, 50, 30, "n")
    white_chapal_road.update_dicto(white_chapal_road, 3)

    community_chest1 = my_property_class(main_frame, "community chest", 10, 8, width, 140)
    community_chest1.update_dicto(community_chest1, 2)

    old_kent_road = my_property_class(main_frame, "old kent road", 10, 9, width, 140, "brown", 2, 60,
                                      10, 30, 90, 160, 250, 50, 50, 30, "n")
    old_kent_road.update_dicto(old_kent_road, 1)

    go_box = my_property_class(main_frame, "go box", 10, 10, 160, 140)
    go_box.update_dicto(go_box, 0)

    # left lane

    pall_mall = my_property_class(main_frame, "pall mall", 9, 0, 160, height, "pink", 10, 140,
                                  50, 150, 450, 625, 750, 100, 50 * 2, 70, "e")
    pall_mall.update_dicto(pall_mall, 11)

    electric_company = my_property_class(main_frame, "electric company", 8, 0, 160, height)
    electric_company.update_dicto(electric_company, 12)

    white_hall = my_property_class(main_frame, "white hall", 7, 0, 160, height, "pink", 10, 140,
                                   50, 150, 450, 625, 750, 100, 50 * 2, 70, "e")
    white_hall.update_dicto(white_hall, 13)

    northumber_ld_avenue = my_property_class(main_frame, "northumberl'd avenue", 6, 0, 160, height, "pink", 12, 160, 60,
                                             180, 500, 700, 900, 100, 100, 80, "e")
    northumber_ld_avenue.update_dicto(northumber_ld_avenue, 14)

    marylebone_station = my_property_class(main_frame, "marltbone station", 5, 0, 160, height)
    marylebone_station.update_dicto(marylebone_station, 15)

    bow_street = my_property_class(main_frame, "bow street", 4, 0, 160, height, "orange", 14, 180,
                                   70, 200, 550, 750, 950, 100, 50 * 2, 90, "e")
    bow_street.update_dicto(bow_street, 16)

    community_chest2 = my_property_class(main_frame, "community chest", 3, 0, 160, height)
    community_chest2.update_dicto(community_chest2, 17)

    marlborough_street = my_property_class(main_frame, "marlborough street", 2, 0, 160, height, "orange", 14, 180,
                                           70, 200, 550, 750, 950, 100, 50 * 2, 90, "e")
    marlborough_street.update_dicto(marlborough_street, 18)

    vine_street = my_property_class(main_frame, "vine street", 1, 0, 160, height, "orange", 16, 200,
                                    80, 220, 600, 800, 1000, 100, 50 * 2, 100, "e")
    vine_street.update_dicto(vine_street, 19)

    monopoly_dis = tk.Label(main_frame, text="Monopoly", bg="tomato1", fg="white")
    monopoly_dis.grid(row=5, column=5)

    sf_width = 8 * width + 2
    sf_height = 3 * height
    status_frame = tk.LabelFrame(main_frame, text="Status Box", bg="light green", fg="black",
                                 highlightbackground="black", highlightthickness=1, width=sf_width, height=sf_height)
    status_frame.grid(rowspan=4, columnspan=9, row=1, column=1)


def final_stage_tweaks():
    print("final stage tweaking")
    global data_holder
    del data_holder["color responses"]
    print(data_holder)
    global rd_obj
    rd_obj = roll_dice_class()

    seek_chance()

    recv_data_updates_thread = threading.Thread(target=recv_data_updates())
    recv_data_updates_thread.start()


def recv_data_updates():
    print("recving data updates")
    while True:
        time.sleep(3)
        data_update = pickle.loads(client.recv(1024))
        print(data_update)

        if len(data_update) == 3:
            data_holder["game info"][data_update[0]][data_update[1]] = data_update[2]
            print(data_holder["game info"])

        elif len(data_update) == 2:
            data_holder[data_update[0]] = data_update[1]
            print(data_holder["game info"])

        else:
            if data_update == "end my turn":
                # ignore as already the updates are sent before(from server) and whose chance it wasn't then seek chance would do the
                # work
                seek_chance()

        # run update info method here


def seek_chance():
    time.sleep(5)
    if data_holder["chance"] == data_holder["player chances"][username]:
        print("My Chance")
        rd_obj.show_dice_btn()
        # other things will be handled by the server and our data update method



class roll_dice_class:

    def __init__(self):
        print("obj created for dice")

    def show_dice_btn(self):
        self.roll_dice_d = tk.Button(main_frame, text="Roll Dice!", bg="orange", font=font,
                                     command=lambda: self.virtual_dice())
        self.roll_dice_d.grid(row=6, column=6)

    def virtual_dice(self):
        self.roll_dice_d.grid_forget()
        self.dice_roll1 = random.randint(1, 6)
        self.dice_roll2 = random.randint(1, 6)
        self.dice_roll = self.dice_roll1 + self.dice_roll2
        self.show_dice = tk.StringVar()
        self.label_dice = "Dice Roll = " + str(self.dice_roll)
        self.show_dice.set(self.label_dice)
        self.rd_label = tk.Label(main_frame, textvariable=self.show_dice, bg="green", fg="orange", width=12, height=2)
        self.rd_label.grid(row=7, column=5)

        self.end_turn = tk.Button(main_frame, text="End Turn!", font=font, command=lambda: self.end_turn_clicked())
        self.end_turn.grid(row=6, column=6)

        # send our server so it munches down the data
        client.send(pickle.dumps((username, "position", self.dice_roll)))
        # then the data muncher on our side will recv and update the screen

    def end_turn_clicked(self):
        client.send(pickle.dumps("end my turn"))
        self.end_turn.grid_forget()
        self.roll_dice_d.grid(row=6, column=6)


container.mainloop()
