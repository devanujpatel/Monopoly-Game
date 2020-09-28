import socket, threading, pickle

# create a af_inet streaming server
server = socket.socket()
server.bind(("", 9999))
server.listen()

HEADER = 10

# a dictionary that contains each and every room created and its data about players
rooms = {}
# a dictionary which will contain information which is sent to client many times during the course of the game
room_game_info = {}
# a dicto which will contain socket objects of each and every player in a particular room
room_player_objs = {}

existing_rooms = []
# start making rooms with no. 100
room = 100

class threaded_Client(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr

    def run(self):
        global rooms, room
        print("Running: " + threading.Thread.getName(self))
        print("waiting for client", self.addr, "to send further action msg!")
        # wait for client to send whether he/she wants to join a room or create a room
        what_to_do = (self.client.recv(16).decode('utf-8'))
        print("recved what to do msg from client")

        # create a room
        if what_to_do == "create room":
            self.create_room()

        # join a room
        if what_to_do == "join room":
            self.join_room()

    def allocate_chance_num(self):
        # increment chance alloc num by 1
        rooms[self.room]["chance alloc num"] += 1
        # return the chance -1 to allocate the chance num to player
        return rooms[self.room]["chance alloc num"] - 1
        # one is subtracted while returning above as we added one before
        # this is so as we need to add one and also return chance num to player
        # if we wrote return before and increment later then the execution of the function will stop at the return
        # statement and incrementation of chance num wouldn't happen!


    def create_room(self):
        global rooms, room
        # give our host player a room no.
        self.room = room
        print(self.room)
        # add the particular room no. in existing rooms list to later know that the room exists
        existing_rooms.append(self.room)
        print(existing_rooms)
        # increment for any other player who creates a new room as we want to give new room num to each room created
        room += 1
        print("next room created will be", str(room))

        # recv username from the player for that particular game
        # this is asked inside the if statement and not outside as later a save game feature will be available and
        # the player might have to choose who he/she is from the saved room

        # receiving username length to later receive whole username
        self.username_length = self.client.recv(HEADER).decode('utf-8')
        self.username_length = int(self.username_length)

        # now recv the username with buffer size = length of username received earlier
        self.username = str(self.client.recv(self.username_length).decode('utf-8'))
        print("received username from", self.addr, ":", self.username, "for room", self.room)

        print(self.username, "is creating a room.")
        # the rooms dicto will be updated with a room no. and other necessary information
        rooms.update({self.room: {"host": self.username, "status": "looking for players",
                              "players list": [self.username],"chance alloc num":0}})
        room_player_objs.update({self.room:{"players": {self.username: self.client}}})

        self.chance = self.allocate_chance_num()
        print(self.username,str(self. chance))
        # send our host the players in his room (at the moment it would be only one player i.e the host itself)
        self.client.send(pickle.dumps(rooms[self.room]["players list"]))

        # recv a msg to know that host wants to start the game -- recall blocking sockets
        self.start_game = self.client.recv(24)
        rooms[self.room]["status"] = "room locked temp"
        print("starting the game for room", self.room, "whose host is", self.username)

        # sending all the players a msg to start the game so our client side code knows to update the screen
        for player in rooms[self.room]["players list"]:
            if player != rooms[self.room]["host"]:
                print("sending to", player)
                room_player_objs[self.room]["players"][player].send(pickle.dumps("start game"))
        print("successfully sent msg to all the players")
        rooms[self.room]["status"] = "looking for players"

    def recv_room_num(self):
        self.room = self.client.recv(16).decode('utf-8')
        self.room = int(self.room)
        self.check_recved_room_num()

    def check_recved_room_num(self):
        if self.room not in existing_rooms:
            # if room doesnt exist then notify the client about the same
            self.client.send(bytes("room doesn't exist", 'utf-8'))
            self.recv_room_num()

        elif self.room in existing_rooms:
            if rooms[self.room]["status"] == "looking for players":
                self.client.send(bytes("joined successfully", 'utf-8'))

                # receiving username length to later receive whole username
                self.username_length = self.client.recv(HEADER).decode('utf-8')
                self.username_length = int(self.username_length)
                self.username = str(self.client.recv(self.username_length).decode('utf-8'))
                print("received username from", self.addr, ":", self.username, "for room", self.room)

                room_player_objs[self.room]["players"][self.username] = self.client
                rooms[self.room]["players list"].append(self.username)
                print(rooms)
                # self.client.send(pickle.dumps(rooms[self.room]["players list"]))
                # send all the players the new list
                for player in rooms[self.room]["players list"]:
                    room_player_objs[self.room]["players"][player].send(pickle.dumps(rooms[self.room]["players list"]))

            elif rooms[self.room]["status"] == "room locked temp":
                # send the client that room is locked
                # locking the room is in the hands of the host but when the host starts the actual game
                # then for some seconds the room will be locked
                # then again it will be unlocked as it is the default though the host can lock it later
                # the room was locked temporarily as the client side code can only recv on thing at a time
                # and it would already be looking for new players list incase someone new joins
                # whenever someone new joins the new comer sends all the pther players the new updated players list
                # but when the host starts the game all the clients need to recv it so the room is lockes temporarily
                # so that no new player can join the room and send the new players list when the host is trying to start
                # the game ----- this is a precautionary measure this is to handle a situation where the starting of game command
                # from the host and joining of a new player doesn't collide so that the client code
                # do not gets confused what it has to recv
                self.client.send(bytes("unable to join temp"))
                # the client side code will then inform our client to try entering the room after a few seconds
                self.recv_room_num()
                # new idea here - do a while loop so that the player joins automatically when the room is again unlocked
                # thus our client doesn't have to send to join room again
            elif rooms[self.room]["status"] == "room locked":
                self.client.send(bytes("room locked",'utf-8'))
                self.recv_room_num()

            # may add a else here for handling some extreme cases and send clinet: some error occured plz try again

    def join_room(self):
        self.recv_room_num()


while True:
    client, addr = server.accept()
    print("Accepted connection from", addr)
    print("creating new thread for", addr)
    client_thread = threaded_Client(client, addr)
    client_thread.start()
    print("Looking for more clients in main thread")

# TODO
#   give timeouts so that you can reomove a person who is inactive for a long time like 120 seconds or 3 times inactive for 30 sec
#   improve gui looks
#   verify username (is it pre occupied or client sent an empty string,etc...)
#   handle input erros from client side like client sent a str instead of room int
#   dont allow to start game if only host is in the room and also automatically start game when 8 players join

# ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
# what happens when server sends something but the client didnt recv it as the client has lost connection

# when u send the length of msg using the HEADER technique then recv whole msg then we use recv two times one time
# on recver side but send once on the sender side????