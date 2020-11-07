import socket, threading, pickle, time

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

# for holding token directions of a room
token_dir = {}

# clients whom we need to send existing room numbers
send_room_num_clients = []

# a list to contain all info to be sent to client in send_room_num_clients
send_room_info_list = {}

existing_rooms = []
# start making rooms with no. 100
room = 100

def send_room_nums():
    if len(send_room_num_clients) != 0:
        send_item = []

        if len(send_room_info_list) != 0:
            for r in send_room_info_list.values():
                send_item.append(r)

            for client in send_room_num_clients:
                try:
                    print("sending to client",client)
                    client.send(pickle.dumps(send_item))
                except ConnectionError:
                    send_room_num_clients.remove(client)

class threaded_Client(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr

    def run(self):
        global rooms, room
        print("Running: " + threading.Thread.getName(self))
        print("waiting for client to send further action msg!", threading.Thread.getName(self))
        # wait for client to send whether he/she wants to join a room or create a room
        what_to_do = (self.client.recv(16).decode('utf-8'))
        print("recved what to do msg from client", threading.Thread.getName(self))

        # create a room
        if what_to_do == "create room":
            self.create_room()

        # join a room
        if what_to_do == "join room":
            self.join_room()

    def create_room(self):
        global rooms, room

        # recv username from the player for that particular game
        # later a save game feature will be available and
        # the player might have to choose who he/she is from the saved room

        # receiving username length to later receive whole username
        self.username_length = self.client.recv(HEADER).decode('utf-8')
        self.username_length = int(self.username_length)

        # now recv the username with buffer size = length of username received earlier
        self.username = str(self.client.recv(self.username_length).decode('utf-8'))

        print(self.username)

        # give our host player a room no.
        self.room = room
        print(self.room)
        # add the particular room no. in existing rooms list to later know that the room exists
        existing_rooms.append(self.room)

        # increment for any other player who creates a new room as we want to give new room num to each room created
        room += 1
        print("next room created will be", str(room))

        print("received username from", self.addr, ":", self.username, "for room", self.room)

        print(self.username, "is creating a room.")
        # the rooms dicto will be updated with a room no. and other necessary information the game info key is the
        # main key in which the game data will be stored and sent to all the clients at the start of the game after
        # which the server and all the clients will maintain it according to the instructions sent
        rooms.update({self.room: {"host": self.username, "status": "looking for players", "color responses": [0, [],{}],
                                  "players list": [], "chance alloc num": 0, "game info": {}, "player chances": {},
                                  "chance": 0,"rounds completed": 0,"token dir":{} ,"send flag": True}})

        # now that the room is properly established we can send it to our clients who want to join a room
        send_room_info_list.update({self.room:[self.room, self.username,1]})
        send_room_nums()

        # for storing and then allocating different poistions to players to avoid overlapping of tokens (these are
        # sticky options of tkinter)
        token_dir.update({self.room:["N","S","E","W","NE","SE","NW","SW"]})
        # contains the client objects of particular room
        room_player_objs.update({self.room:{}})

        # the names are self explanatory
        self.allocate_chance_num()
        self.new_player_dicto_update()

        print(self.username+"'s chance is", str(self.chance))
        # send our host the players in his room (at the moment;it would be only one player i.e the host itself)
        self.client.send(pickle.dumps(rooms[self.room]["players list"]))

        # recv a msg to know that host wants to start the game -- recall blocking sockets
        self.start_game = self.client.recv(24)
        rooms[self.room]["status"] = "room locked temp"
        rooms[self.room].update({"start game count":0})
        print("starting the game for room", self.room, "whose host is", self.username)
        print("sending to", self.username)
        # when recved by client he/she starts to recv things sent further after, this is a type of signal
        room_player_objs[self.room][self.username].send(pickle.dumps("start game"))
        room_player_objs[self.room][self.username].send(pickle.dumps(rooms[self.room]))
        # just keeping a track of players
        rooms[self.room]["start game count"] += 1

        if rooms[self.room]["start game count"] == len(rooms[self.room]["players list"]):
            print("successfully sent msg to all the players, last player", self.username)
            rooms[self.room]["status"] = "game started"
        else:
            pass

        # play game...
        self.play_game()

        # there are three states of status - room locked, looking for players and game started
        # for a room to be locked status should be room locked ,either the game has starteed or not in this state no more players will be able to join
        # else it will be-looking for players or game started
        # players can join the room in game started or in looking for players mode but no when room is locked

    def allocate_chance_num(self):
        # chance alloc num is a number which will be allocated to a player when he joins
        self.chance = rooms[self.room]["chance alloc num"]
        # then increment the num as we do not want two people with same chance
        rooms[self.room]["chance alloc num"] += 1

    def new_player_dicto_update(self):
        #  this function will run whenever a player joins, this is to store/update data in a dictionary
        # the values are appropriate for a fresh game (new game)
        # if a saved game is to be started again then never ever call this function!

        rooms[self.room]["game info"].update(
            {self.username: {"color": None, "money": 1800, "position": 0, "properties": {}, }})
        # the "properties" key will have all the prop.s which the player owns along with it status which can be-
        # mortgaged or normal and the no. of houses on it for 0 = no house , 1 = 1 house and so on and 5 for a hotel

        # more keys may be added later as needed!

        # add the player in the chances list(stored in rooms dicto) so that we know whose chance it is and we can
        # react acc.
        rooms[self.room]["player chances"].update({self.username: self.chance})

        # add him in players list
        rooms[self.room]["players list"].append(self.username)

        # in the objects dicto also which was created by the host
        room_player_objs[self.room].update({self.username: self.client})

        # for avoiding token overlapping as discussed earlier
        rooms[self.room]["token dir"].update({self.username: token_dir[self.room].pop(-1)})

    def join_room(self):
        send_room_num_clients.append(self.client)
        send_room_nums()
        print("CLIENT HERRE",self.client)
        self.recv_room_num()

    def recv_room_num(self):
        self.room = self.client.recv(16).decode('utf-8')
        self.room = int(self.room)
        self.check_recved_room_num()

    def check_recved_room_num(self):
        if self.room not in existing_rooms:
            # if room doesnt exist then notify the client about the same
            self.client.send(bytes("room doesn't exist", 'utf-8'))
            # again wait for client to send room num
            self.recv_room_num()

        elif self.room in existing_rooms:

            if rooms[self.room]["status"] == "looking for players":
                send_room_num_clients.remove(self.client)
                self.client.send(bytes("joined successfully", 'utf-8'))

                # receiving username length to later receive whole username
                self.username_length = self.client.recv(HEADER).decode('utf-8')
                self.username_length = int(self.username_length)
                self.username = str(self.client.recv(self.username_length).decode('utf-8'))
                print("received username from", self.addr, ":", self.username, "for room", self.room)

                self.allocate_chance_num()
                self.new_player_dicto_update()
                print(self.username, "'s chance is", str(self.chance))
                print(rooms)

                # send all the players the new players list
                for player in rooms[self.room]["players list"]:
                    room_player_objs[self.room][player].send(pickle.dumps(rooms[self.room]["players list"]))

                send_room_info_list[self.room][2] = len(rooms[self.room]["players list"])
                send_room_nums()

                # then check in a while true loop  for status - room locked temp(rlt) cuz when host starts the game the stat is changed to rlt
                while True:
                    time.sleep(0.5)
                    if rooms[self.room]["status"] == "room locked temp":
                        print("sending to", self.username)
                        room_player_objs[self.room][self.username].send(pickle.dumps("start game"))
                        room_player_objs[self.room][self.username].send(pickle.dumps(rooms[self.room]))
                        rooms[self.room]["start game count"] += 1

                        if rooms[self.room]["start game count"] == len(rooms[self.room]["players list"]):
                            print("successfully sent msg to all the players", self.username)
                            rooms[self.room]["status"] = "game started"
                        else:
                            pass
                        print('running play game')
                        self.play_game()
                    else:
                        time.sleep(0.5)

            # elif rooms[self.room]["status"] == "game started":
            # will be developed soon!

            elif rooms[self.room]["status"] == "room locked temp":
                # send the client that room is locked
                # locking the room is in the hands of the host but when the host starts the actual game
                # then for some seconds the room will be locked(room locked temp)
                # then again it will be unlocked as it is the default though the host can lock it later
                # the room was locked temporarily as the client side code can only recv one thing at a time
                # and it would already be looking for new pltheayers list incase someone new joins
                # whenever someone new joins the new comer sends all the other players the new updated players list
                # but when the host starts the game all the clients need to recv the msg so the room is locked temporarily
                # so that no new player can join the room and send the new players list when the host is trying to start
                # the game ----- this is a precautionary measure this is to handle a situation where the starting of game command
                # from the host and joining of a new player doesn't collide so that the client code
                # do not gets confused what it has to recv and also the client side thread on the server gets to know what is happening
                self.client.send(bytes("unable to join temp"))
                # the client side code will then inform our client to try entering the room after a few seconds
                self.recv_room_num()
                # new idea here - do a while loop so that the player joins automatically when the room is again unlocked
                # thus our client doesn't have to send to join room again
            elif rooms[self.room]["status"] == "room locked":
                self.client.send(bytes("room locked", 'utf-8'))
                self.recv_room_num()

            # this is only while in developing stage as "game started" mode is not covered yet
            else:
                self.client.send(bytes("error", 'utf-8'))
                self.client.close()

    def play_game(self):

        # send flag = True means u are good to go and send flag False means wait for sometime and then send when
        # send flag is True

        # first of all we get the favourite color of each player
        rooms[self.room]["color responses"][2].update({self.username:"not ready"})
        self.fav_color = pickle.loads(self.client.recv(1024))
        rooms[self.room]["color responses"][2].update({self.username:"ready"})

        rooms[self.room]["game info"][self.username]["color"] = self.fav_color
        # + color responses
        rooms[self.room]["color responses"][0] += 1
        rooms[self.room]["color responses"][1].append(self.fav_color)
        self.sent = []
        self.not_reachable = []

        # after the for loop we will know how many players are left to send the color responses
        for player in rooms[self.room]["players list"]:
            if rooms[self.room]["color responses"][2][player] == "ready" and player not in self.sent:
                room_player_objs[self.room][player].send(pickle.dumps(self.fav_color))
                self.sent.append(player)
            elif rooms[self.room]["color responses"][2][player] == "not ready":
                self.not_reachable.append(player)
        print(self.sent)
        print(self.not_reachable)
        # send the leftover players the color
        while True:
            for player in self.not_reachable:
                time.sleep(0.3)
                if rooms[self.room]["color responses"][2][player] == "ready":
                    room_player_objs[self.room][player].send(pickle.dumps(self.fav_color))
                    self.sent.append(player)
                    self.not_reachable.remove(player)

                if len(self.not_reachable) == 0:
                    for player in rooms[self.room]["players list"]:
                        room_player_objs[self.room][player].send(pickle.dumps("end"))
                    break

        # after this we start the actual game!
        # main game

    def main_game(self):

        # a client conn only gets closed when he/she leaves
        # when while loop (2) gets over their is a doubt whether the client is disconnected
        # so when the main while loop(1) ends the conn will get over

        # when the player leaves many things can be done- stop game , continue and forget the left player

        # can make a option to save and leave game when one player leaves ,to the host
        # if host decides to continue the game then the player will be erased (new option on the way)
        # elif host decides to save the game then the game will end, inference drawn, and saved too(ofcourse)
        # host can simply just end the game also
        # it is to be decided how to manage the game after the removal of the player (as we can allow to let the player join again)
        # if host leaves the whole game is disbanded and option to save the game goes to player 1

        # the loop(2) is responsible to run the game
        # whereas the loop(1) is responsible to confirm disconnections

        # loop (2) - LOOP OF GAME
        while True:
            # look out for our client; if something is sent we need to MUNCH DOWN THE DATA

            # the name is data TUP as we are gonna communicate via tuples which contain change orders by our client
            # FORMAT: (username,what needs to be changed, update value)
            # it is to be read as change xyz of abc name to pqr
            # or else it could be : (what to do , player desig) for cases like end turn, leave game, end game,etc...
            try:
                while True:

                    data_tup = self.client.recv(1024)
                    if data_tup:
                        pickle.loads(data_tup)
                        break
                    else:
                        pass
            except ConnectionResetError as e:
                print(e, self.username, self.room)
                # give loop(2) chance to assess the situation then if client has to leave then break from main loop too
                # if not then continue to run loop(1) which will then run loop(2)
                return "check if active"

            # if it is to end our turn then do so; sent only when 30 sec timeout happens or end turn btn clicked on client's side
            if data_tup == "end my turn":
                # increase chance num by one
                rooms[self.room]["chance"] += 1
                # while increasing chance we also need to see if chance number is within limit
                if rooms[self.room]["chance"] == len(rooms[self.room]["players list"]):
                    rooms[self.room]["rounds completed"] += 1
                    rooms[self.room]["chance"] = 0

            # player leaves gracefully!
            elif data_tup[0] == "leave" and data_tup[1] == "player":
                leave_confirmation_status = "ask again player"
                return leave_confirmation_status

            elif data_tup[0] == "leave" and data_tup[1] == "host":
                leave_confirmation_status = "ask again host"
                return leave_confirmation_status

            # host sends to end game
            elif data_tup[0] == "end game" and data_tup[1] == "host":
                leave_confirmation_status = "ask to save"
                return leave_confirmation_status

            else:
                # LET'S MUNCH DOWN OUR DATA
                rooms[self.room][[data_tup][0]][[data_tup][1]] = [[data_tup][2]]
                # send the same to others
                rooms[self.room]["send flag"] = False
                for player in rooms[self.room]["players list"]:
                    if player != data_tup[0]:
                        room_player_objs[self.room][player].send(pickle.dumps(data_tup))
                    else:
                        pass
                rooms[self.room]["send flag"] = True

    def assess_situation(self):

        # this is while True no. (1)
        while True:

            # constantly run the loop(2) to play game then the main_game fnc will return for situation handling
            lcs = self.main_game()

            # assess the situation possible situations: 1> CLIENT LEAVES GRACEFULLY 2> CLIENT GETS DISCONNECTED (
            # doubt if player is active) 3> HOST ENDS THE GAME 4> HOST LEAVES ABRUPTLY
            # situation 1 : make the player leave but keep his dicto alive, ->then ask host if he wants to still continue the game if yes then
            # erase the player dicto and distribute props to bank and if no then ask host to save the game
            # sit 2,the player will be asked if he/she is still in the game with a timeout of 20 seconds if timeout happens
            # then proceed as situation 1 after '->'
            # situation 3 : ask host to save game
            # situation 4 : ask player1 the option to end and save game

            print(lcs)
            # lcs = leave_confirmation_status and wtd = what_to_do
            if lcs == "check if active":
                wtd = self.check_if_active()
            if lcs == "ask again host":
                wtd = self.confirm_leave("host")
            if lcs == "ask again player":
                wtd = self.confirm_leave("player")
            if lcs == "ask to save":
                wtd = self.end_game_confirm()

            # more lcs on the way

        # ACC TO WTD(what to do) REACT FURTHER (like run a fnc) AND THEN AFTER THAT RESPECTIVE FNC has completed execution REACT ACC. TO THE NEW WTD I.E PROBABLY BREAK
        # OR RUN MAIN_GAME_AGAIN WHICH MEANS TO JUST CONTINUE THE LOOP OF GAME AS USUAL


    # still left to do, associated with the main game and play game functions

    def confirm_leave(self, player_desig):
        pass
        # return a value ; active or not , if host not active then ask player1
        # if player not active then ask host his options

    def save_room(self):
        pass

    def end_game_confirm(self):
        # it is ; ask to save room or end game now
        pass

    def end_game(self):
        pass

    def check_if_active(self):
        pass

    def close_conn(self, conn):
        pass

    def read_saved_game(self):
        pass

    def waiting_mode(self):
        pass


while True:
    time.sleep(3)
    client, addr = server.accept()
    print("Accepted connection from", addr)
    print("creating new thread")
    client_thread = threaded_Client(client, addr)
    client_thread.start()
    print("Looking for more clients in main thread")
    print(threading.enumerate())
    time.sleep(3)

# TODO
#   give timeouts so that you can reomove a person who is inactive for a long time like 120 seconds or 3 times inactive for 30 sec
#   improve gui looks
#   verify username (is it pre occupied or client sent an empty string,etc...)
#   handle input erros from client side like client sent a str instead of room int
#   dont allow to start game if only host is in the room and also automatically start game when 8 players join
#   see the check recved room num comments for ndew features update   (3)
#   also make a backup feature in the game (players can take backup at regular intervals)
#   think of a way to let player join again with same game status as before
#   GIVE DEFAULT COLOR to players when they do not choose any color
#   see below comments and resolve them and also see keep for the doubts

# ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
# what happens when server sends something but the client didnt recv it as the client has lost connection
# when u send the length of msg using the HEADER technique then recv whole msg then we use recv two times one time
# on recver side but send once on the sender side????
