import socket
import threading
import pickle
import select

# create our server socket : defaults to AF_INET and streaming socket!
server = socket.socket()
server.bind(("",9999))
server.listen()

HEADER = 10
sockets_list = [server]

# dictionary that handles everythong
rooms = {}
room = 100

# start new thread for recieving username and etc. stuff (this will also be the thread which will handle the game for the player)
class client_class(threading.Thread):
    def __init__(self, client, addr,read_socks):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr
        self.read_socks = read_socks

    def run(self):
        # recv username , new room or join room , favourite color, etc...
        # do further things like waiting or playing
        global room
        # get length of usernmame and then buffer the whole username
        user_name_length = self.client.recv(HEADER)
        user_name_length = int(user_name_length.decode('utf-8'))
        username = self.client.recv(user_name_length)

        self.username = username
        # inform us about the new connection
        print(f"Connection from {username},{self.client}{self.addr} has been establieshed successfully !!!")
        # send a msg to client about the same
        msg_to_client = "Connection established successfully, enjoy your game of monopoly!"
        self.client.send(bytes(msg_to_client,"utf-8"))

        # recv from the client whether he/she wants to create a room or join a room ! (0 TO CREATE A ROOM AND 1 TO JOIN A ROOM.)
        what_to_do = self.client.recv(8)
        what_to_do = what_to_do.decode('utf-8')

        if what_to_do == 0:
            self.create_room()
            # to give the next room created a unique room name
            room += 1

        if what_to_do == 1:
            # do something to join a room
            pass

    def create_room(self):
        # create a room
        # the first item in the players list(which is the value of 'players' key below) will be the host and further players will be added later
        self.room_dicto = {"players":[self.username]}

        # also add it in the main rooms dictionary
        rooms.update({room:self.room_dicto})

        # a variable waiting which could be True or False, if False then start game- start game will only run when host tells to do so
        waiting = self.client.recv(16)
        # start the game when received (recall about blocking sockets!)
        # can only send str so "false"
        if waiting == "false":
            self.start_game()
        # may have to do some modifications


    def start_game(self):
        # players should see the main game frame

        self.info = {"player_num":len(self.room_dicto['players']),}
        self.client.send(bytes("true",'utf-8'))



while True:
    client, addr = server.accept()
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    # creating obj of Client hope it overwrites the obj name everytime a new player joins
    handling_thread = client_class(client, addr,read_sockets)
    handling_thread.start()



