import socket
import threading

server = socket.socket()
server.bind(("127.0.0.1",9999))
server.listen(8)

HEADER = 10
sockets_list = [server]

# dictionary that handles everythong
rooms = {}
room = 100

class Client(threading.Thread):
    def __init__(self,client,addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr

    def run(self):
        global room
        print(thread.getName())
        user_name_length = self.client.recv(HEADER)
        user_name_length = int(user_name_length.decode('utf-8'))
        username = self.client.recv(user_name_length)
        print(username)
        self.username = username
        msg_to_client = "Connection established successfully, enjoy your game of monopoly!"
        msg = f"{len(msg_to_client):<{HEADER}}" + msg_to_client
        self.client.send(bytes(msg, "utf-8"))

        # recv from the client whether he/she wants to create a room or join a room ! (0 TO CREATE A ROOM AND 1 TO JOIN A ROOM.)
        what_to_do = self.client.recv(8)
        what_to_do = what_to_do.decode('utf-8')

        if what_to_do == "false":
            self.create_room()
            print("created room", room)
            # to give the next room created a unique room name
            room += 1


        if what_to_do == 1:
            # do something to join a room
            print("joining room")
            pass

    def create_room(self):
        # create a room
        # the first item in the players list(which is the value of 'players' key below) will be the host and further players will be added later
        self.room_dicto = {"players":[self.username]}
        self.sockets = {self.username:self.client}
        # also add it in the main rooms dictionary
        rooms.update({room:{"player_names":self.room_dicto,self.username:self.client}})
        c = rooms[room][self.username]
        c.send(bytes("hey there !",'utf-8)'))
        print("creating room", room)
        print(self.room_dicto)
        print(rooms)
        # a variable waiting which could be True or False, if False then start game- start game will only run when host tells to do so
        waiting = self.client.recv(16)
        waiting = waiting.decode('utf-8')
        print(waiting)
        # start the game when received (recall about blocking sockets!)
        # can only send str so "false"
        if waiting == "false":
            print("waiting = false")
            self.start_game()

    def start_game(self):
        print("starting game !")
        # players should see the main game frame

        self.info = {"player_num":len(self.room_dicto['players']),}
        self.client.send(bytes("true",'utf-8'))



while True:
    client, addr = server.accept()
    print(f"accepted connection from {addr} has been established !!!")
    thread = Client(client,addr)
    thread.start()




