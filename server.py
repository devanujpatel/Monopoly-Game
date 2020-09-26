import socket, threading, pickle

# create a af_inet streaming server
server = socket.socket()
server.bind(("", 9999))
server.listen()

HEADER = 10

# a dictionary that contains each and every room created and its data about players
rooms = {}
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
        # wait for client to send whether he/she wants to join a room(0) or create a room(1)
        what_to_do = int(self.client.recv(16).decode('utf-8'))
        print("recved what to do msg from client")

        # create a room
        if what_to_do == 1:
            
            # give our host player a room no.
            self.room = room
            # add the particular room no. in existing rooms list to later know that the room exists
            existing_rooms.append(room)
            # increment for any other player who creates a new room as we want to give new room num to each room created
            room += 1
            print("next room created will be", str(room))

            # recv username from the player for that particular game
            # this is asked inside the if statement and not outside as later a save game feature will be available and 
            # the player might have to choose who he/she is from the saved room  
            
            # receiving username length to later receive whole username
            self.username_length = self.client.recv(HEADER).decode('utf-8')
            self.username_length = int(self.username_length)
            self.username = str(self.client.recv(self.username_length).decode('utf-8'))
            print("received username from", self.addr, ":", self.username,"for room",room)
            
            print(self.username,"is creating a room.")
            # the rooms dicto will be updated with a room no. and other necessary information
            rooms.update({room: {"host":self.username,"status":"looking for players","players": {self.username: self.client},"players list":[self.username]}})
            
            # send our host the players in his room (at the moment it would be only one player i.e the host itself)
            self.client.send(pickle.dumps(rooms[self.room]["players list"]))

            # recv a msg to know that host wants to start the game -- recall blocking sockets
            start_game = self.client.recv(24).decode('utf-8')
            rooms[self.room]["status"] = "room locked"
            print("starting the game for room",self.room,"whose host is",self.username)
            
            # sending all the players a msg to start the game so they our client side code knows to update the screen
            for player in rooms[self.room]["players list"]:
                print("sending to",player)
                rooms[self.room]["players"][player].send(bytes("start game",'utf-8'))
            print("successfully sent msg to all the players")

        # join a room
        if what_to_do == 0:
            self.room_num = self.client.recv(16).decode('utf-8')
            self.room_num = int(self.room_num)
            if self.room_num not in existing_rooms:
                # if room doesnt exist then notify the client about the same
                self.client.send(bytes("room doesnt exist",'utf-8'))

            if self.room_num in existing_rooms:
                self.room = self.room_num
                # receiving username length to later receive whole username
                self.username_length = self.client.recv(HEADER).decode('utf-8')
                self.username_length = int(self.username_length)
                self.username = str(self.client.recv(self.username_length).decode('utf-8'))
                print("received username from", self.addr, ":", self.username, "for room", self.room)

                if rooms[self.room]["status"] == "looking for players":
                    rooms[self.room]["players"][self.username] = self.client
                    rooms[self.room]["players list"].append(self.username)
                    print(rooms)
                    # self.client.send(pickle.dumps(rooms[self.room]["players list"]))
                    # send all the players the new list
                    for player in rooms[self.room]["players list"]:
                        print(player)
                        print(rooms[self.room]["players"][player])
                        rooms[self.room]["players"][player].send(pickle.dumps(rooms[self.room]["players list"]))

                elif rooms[self.room]["status"] == "room locked":
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

                    self.client.send(bytes("unable to join"))
                    # also later join the room when it is unlocked



while True:
    client, addr = server.accept()
    print("Accepted connection from", addr)
    print("creating new thread for", addr)
    client_thread = threaded_Client(client, addr)
    client_thread.start()
    print("Looking for more clients in main thread")

# TODO
#   give timeouts so that you can reomove a person who is inactive for a long time like 120 seconds
#   improve gui looks
"""
# receiving username length to later receive whole username
        self.username_length = self.client.recv(HEADER).decode('utf-8')
        self.username_length = int(self.username_length)
        self.username = str(self.client.recv(self.username_length).decode('utf-8'))
        print("received username from", self.addr, ":", self.username)"""