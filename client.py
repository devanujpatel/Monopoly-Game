import socket, pickle, threading
import tkinter as tk

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

# make a grid on the container so as to make placing easier
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=0)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=1)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=2)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=3)
tk.Frame(start_frame,width= width/7,height=height/7).grid(row=0,column=4)

font = ("Courier", 13)

"""# ask for username
username_entry = tk.Entry(start_frame)
ok_but_for_username = tk.Button(start_frame, text= "Okay",font= font,command= lambda :ok_but_for_username_clicked())
username_entry.grid(row=3,column=3)
ok_but_for_username.grid(row=4,column=3)

def ok_but_for_username_clicked():
    ok_but_for_username.grid_forget()
    username_entry.grid_forget()
    username = str(username_entry.get())

    print("sending username")
    username_sendable = f"{len(username):<{HEADER}}"+username
    client.send(bytes(username_sendable,'utf-8'))"""

# give our client a choice of creating or joining a room 
create_room_btn = tk.Button(start_frame,text="Create Room",command=lambda:create_room())
create_room_btn.grid(row=3,column=2)
join_room_btn = tk.Button(start_frame, text="Join Room", command=lambda: join_room())
join_room_btn.grid(row=3, column=4)

def create_room():
    join_room_btn.grid_forget()
    create_room_btn.grid_forget()
    print("sending to create new room!")
    client.send(bytes("create room", 'utf-8'))
    ask_username()
    
def join_room():
    join_room_btn.grid_forget()
    create_room_btn.grid_forget()
    print("sending to join room!")
    client.send(bytes("join room", 'utf-8'))
    ask_room_num()

def ask_username():
    # ask for username
    global ok_but_for_username, username_entry
    username_entry = tk.Entry(start_frame)
    ok_but_for_username = tk.Button(start_frame, text="Okay", font=font, command=lambda: ok_but_for_username_clicked())
    username_entry.grid(row=3, column=3)
    ok_but_for_username.grid(row=4, column=3)

def ok_but_for_username_clicked():
    ok_but_for_username.grid_forget()
    username_entry.grid_forget()
    username = str(username_entry.get())
    print("sending username")
    username_sendable = f"{len(username):<{HEADER}}" + username
    client.send(bytes(username_sendable, 'utf-8'))
    start_game_btn = tk.Button(start_frame, text="Start Game",command = lambda:start_game_host())
    start_game_btn.grid(row=4, column=3)
    check_on_new_thread_npl = recv_new_players_list_thread()
    check_on_new_thread_npl.start()

def ask_room_num():
    global room_num_entry, ok_but_room_num
    room_num_entry = tk.Entry(start_frame)
    room_num_entry.grid(row=2,column=3)
    ok_but_room_num = tk.Button(start_frame, text="Ok",command = lambda:ok_but_room_num_clkd())
    ok_but_room_num.grid(row=2,column=4)

def ok_but_room_num_clkd():
    room_num_entry.grid_forget()
    ok_but_room_num.grid_forget()
    room = room_num_entry.get()
    client.send(bytes(room,'utf-8'))
    status = client.recv(1024).decode('utf-8')

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
        # accept new players list as new players do join and the list needs to be updated
        global check_for_new_players_list_stat
        print("checking for new players list on",threading.Thread.getName(self))
        check_for_new_players_list_stat =  True
        while check_for_new_players_list_stat:

            new_players_list = client.recv(1024)
            if new_players_list:
                new_players_list = pickle.loads(new_players_list)
                if new_players_list == "start game":
                    check_for_new_players_list_stat = False
                    start_game_player()
                else:
                    print("new players list = ", new_players_list)

def start_game_host():
    client.send(bytes("start the game",'utf-8'))
    global check_for_new_players_list_stat
    check_for_new_players_list_stat = False
    print("player started the game")

def start_game_player():
    print("Yo lets play")

def recv_game_details():
    pass

"""def recv_players_list()
    print("recving players list")
    players_in_room = client.recv(1024)
    players_in_room = pickle.loads(players_in_room)
    print(players_in_room)
    
    
    global ok_but_for_username, username_entry
        username_entry = tk.Entry(start_frame)
        ok_but_for_username = tk.Button(start_frame, text="Okay", font=font, command=lambda: ok_but_for_username_clicked())
        username_entry.grid(row=3, column=3)
        ok_but_for_username.grid(row=4, column=3)
        # show the players list
        # recv for new players list on new thread
        print("recving players list on new thread")
        check_thread = recv_new_players_list_thread()
        check_thread.start()
        
        ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
"""



container.mainloop()