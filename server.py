import socket, threading, pickle

# create a af_inet streaming server
server = socket.socket()
server.bind(("", 9999))
server.listen()

HEADER = 10

# a dictionary that contains each and every room created and its data about players
rooms = {}
# start making rooms with no. 100
room = 100


class threaded_Client(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr

    def run(self):
        try:
            global rooms, room
            print("Running: " + threading.Thread.getName(self))
            print("waiting for client", self.addr, "to send username!")
            # receiving username length to later receive whole username
            self.username_length = self.client.recv(HEADER).decode('utf-8')
            self.username_length = int(self.username_length)
            self.username = str(self.client.recv(self.username_length).decode('utf-8'))
            print("received username from", self.addr, ":", self.username)

            print("waiting for client", self.addr, "to send further action msg!")
            what_to_do = int(self.client.recv(16).decode('utf-8'))

            # wait for client to send whether he/she wants to join a room(0) or create a room(1)

            # create a room
            if what_to_do == 1:
                print("Client creating a room.")
                # the rooms dicto will be updated with a room no. and another dicto which includes
                # names of players and their objects
                rooms.update({room: {"players": {self.username: self.client}}})
                print(rooms)
                room += 1
                print("next room created will be", str(room))
                self.client.close()

            # join a room
            if what_to_do == 0:
                print("Client joining a room.")
                room_num = self.client.recv(16).decode('utf-8')
                room_num = int(room_num)
                rooms[room_num]["player names"].append(self.username)
                rooms[room_num]["player objects"].append(self.client)
                print(rooms)

                self.client.close()

        except Exception as e:
            print("an error occured", e)
            # close the connection (later delete from dictionaries)
            self.client.close()


while True:
    client, addr = server.accept()
    print("Accepted connection from", addr)
    print("creating new thread for", addr)
    client_thread = threaded_Client(client, addr)
    client_thread.start()
    print("Looking for more clients in main thread")

# TODO
#   continuously check whether client has disconnected (if disconnected then close)
#   send info of new room created to the host and to players who joined
#   improve gui looks
