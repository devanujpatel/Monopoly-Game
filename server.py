import socket
import threading
import pickle
import select

# create our server socket : defaults to AF_INET and streaming socket!
server = socket.socket()
server.bind(("",9999))
server.listen()

HEADER = 10

# dictionary that handles everythong
rooms = {}
room = 100

notified_players , _, error_list  = select.

# start new thread for recieving username and etc. stuff (this will also be the thread which will handle the game for the player)
class Client(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr
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
        print(f"Connection from {username},{self.client}{addr} has been establieshed successfully !!!")
        # send a msg to client about the same
        msg_to_client = "Connection established successfully, enjoy your game of monopoly!"
        self.client.send(bytes(msg_to_client,"utf-8"))

        # recv from the client whether he/she wants to create a room or join a room ! (0 TO CREATE A ROOM AND 1 TO JOIN A ROOM.)
        what_to_do = self.client.recv(8)
        what_to_do = what_to_do.decode('utf-8')

        if what_to_do == 0:
            self.create_room()
            room += 1

        if what_to_do == 1:
            # do something to join a room
            pass

    def create_room(self):
        # create a room
        # the first item in the players list(which is the value of 'players' key below) will be the host and further players will be aded later
        self.room_dicto = {"players":[self.username]}
        # also add it in the main rooms dictionary
        rooms.update({room:self.room_dicto})

        # add the player(in this case the host) in notified players list
        #notified_players.append(self.client)
        # provide instead the data in the infinte while loop as discussed below


        # wait for more players to join!
        # plan till now is in a infinite while loop and then loop through the self.players list in the self.room_dicto and then provide the new
        # comers with the data till now || ignore the ones in notified sockets as they will be notified already





while True:
    client, addr = server.accept()
    # creating obj of Client hope it overwrites the obj name everytime a new player joins
    handling_thread = Client(client, addr)
    handling_thread.start()



