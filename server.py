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

existing_rooms = []
# start making rooms with no. 100
room = 100

# ------------☺☺☺ INSTRUCTIONS ☺☺☺------------
#  A DETAILED EXPLANATION OF THE DATA STORED IN THE ROOMS DICTIONARY WILL BE SOON ADDED AS A DOCSTRING
#  IN THE END OF THE CODE
# this is so as it is hard to write long comments so all the usages and reasons of the dictionary will soon be added

class threaded_Client(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr

    def run(self):
        global rooms, room
        print("Running: " + threading.Thread.getName(self))
        print("waiting for client to send further action msg!",threading.Thread.getName(self))
        # wait for client to send whether he/she wants to join a room or create a room
        what_to_do = (self.client.recv(16).decode('utf-8'))
        print("recved what to do msg from client", threading.Thread.getName(self))

        # create a room
        if what_to_do == "create room":
            self.create_room()

        # join a room
        if what_to_do == "join room":
            self.join_room()

    def play_game(self):

        # send flag = True means u are good to go and send flag False means wait for sometime and then send when senn
        # flag is True

        # first of all we get the favourite color of each player
        self.fav_color = self.client.recv(1024).decode('utf-8')
        rooms[self.username]["fav_color"] = self.fav_color
        # + color responses
        rooms[self.room]["color responses"][0] += 1
        rooms[self.room]["color responses"][1].update({self.username:self.fav_color})
        # check in while True for color responses == to n_players , then send the list of all colors
        while True:
            if rooms[self.room]["color responses"] == len(rooms[self.room]["players list"]):
                self.client.send(pickle.dumps(rooms[self.room]["color responses"[1]]))
                break

            if rooms[self.room]["color responses"] != len(rooms[self.room]["players list"]):
                time.sleep(0.5)
                pass


        # after this we start the actual game!

        # a client conn only gets closed when he/she leaves
        # so when the main while loop(1) end s the conn will get over
        # when while loop (2) gets over their is a doubt whether the client is disconnected

        # can make a option to save and leave game when one player leaves ,to the host
        # if host decides to continue the game then the player will be erased (new option on the way)
        # elif host decides to save the game then the game will end, inference drawn, and saved too(ofcourse)
        # also host can simply just end the game also
        # it is to be decided how to manage the game after the removal of the player
        # if host leaves the whole game is disbanded and option to save the game goes to player 1

        # the loop(2) is responsible to run the game
        # whereas the loop(1) is responsible to confirm disconnections

        # this is while True no. (1)
        while True:

            # loop (2)
            while True:
                # look out for our client; if something is sent we need to MUNCH DOWN THE DATA

                # the name is data TUP as we are gonna communicate via tuples which contain changes orderes by our client
                # FORMAT: (username,what needs to be changed, update value)
                # it is to be read as change xyz of abc name to pqr
                try:
                    data_tup = pickle.loads(self.client.recv(1024))
                except Exception as e:
                    print(e, self.username , self.room)
                    # give loop(2) chance to assess the situation then if client has to leave then break from main loop too
                    # if not then continue to run loop(1) which will then run loop(2)
                    break

                # if it is to end our turn then do so; sent only when 30 sec timeout happens or end tru btn clicked on
                # client's side
                if data_tup == "end my turn":
                    # increase chance num by one
                    rooms[self.room]["chance"] += 1
                    # while increasing chance we also need to see if chance number is within limit
                    if rooms[self.room]["chance"] == len(rooms[self.room]["players list"]):
                        rooms[self.room]["rounds completed"] += 1
                        rooms[self.room]["chance"] = 0

                # player leaves gracefully!
                elif data_tup == "leave":
                    leave_confirmed = True
                    break

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

        # assess the situation
        # possible situations:
        # 1> CLIENT LEAVES GRACEFULLY
        # 2> CLIENT GETS DISCONNECTED (dooubt if player is active)
        # 3> HOST ENDS THE GAME
        # 4> HOST LEAVES ABRUPTLY
        # situation 1 : make the player leave but keep his dicto alive, ->then ask host if he wants to still continue
        # the game if yes then erase the player dicto and distribute props to bank and if no then ask host to save the game
        # sit 2, the player will be asked if he/she is still in the game with a timeout of 20 seconds then proceed
        # as situation 1 after '->'
        # situation 3 : ask host to save game
        # situation 4 : ask player1 the option to end and save game

        # also make a backup feature in the game
        # think of a way to let player join again with same game status as before




        self.client.close()

    def allocate_chance_num(self):
        """# increment chance alloc num by 1
        rooms[self.room]["chance alloc num"] += 1
        # return the chance -1 to allocate the chance num to player
        return rooms[self.room]["chance alloc num"] - 1
        # one is subtracted while returning above as we added one before
        # this is so as we need to add one and also return chance num to player
        # if we wrote return before and increment later then the execution of the function will stop at the return
        # statement and incrementation of chance num wouldn't happen!"""

        self.chance = rooms[self.room]["chance alloc num"]
        rooms[self.room]["chance alloc num"] += 1

    def new_player_dicto_update(self):
        #  this function will run whenever a player joins, this is to store data in a dictionary
        # the values are appropriate for a fresh game (new game)
        # if a saved game is to be started again then never ever call this function!

        rooms[self.room]["game info"].update({self.username:{"color":None,"money":1800,"position":0,"properties":{},}})
        # the "properties" key will have all the prop.s which thye player owns along with it status which can be- mortgaged
        # or normal and the no. of houses on  it for 0 = no house , 1 = 1 house and so on and 5 for a hotel
        # more keys may be added later as needed!

        # add the player inthe chances list(stored in rooms dicto) soi that we know whose chance it is and we can react acc.
        rooms[self.room]["player chances"].update({self.username:self.chance})

        rooms[self.room]["players list"].append(self.username)

        room_player_objs.update({self.room: {self.username: self.client}})


    def create_room(self):
        global rooms, room
        # give our host player a room no.
        self.room = room
        print(self.room)
        # add the particular room no. in existing rooms list to later know that the room exists
        existing_rooms.append(self.room)

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
        # the game info key is the main key in which the game data will be stored and sent to all the clients at the
        # start of the game after which the server and all the clients will maintain it according to the instructions sent
        rooms.update({self.room: {"host": self.username, "status": "looking for players","color responses":[0,{}],
                              "players list": [],"chance alloc num":0, "game info": {},"player chances":{}, "chance":0,
                              "rounds completed":0, "send flag":True}})

        self.allocate_chance_num()
        self.new_player_dicto_update()
        print(self.username,"'s chance is",str(self. chance))
        # send our host the players in his room (at the moment it would be only one player i.e the host itself)
        self.client.send(pickle.dumps(rooms[self.room]["players list"]))

        # recv a msg to know that host wants to start the game -- recall blocking sockets
        self.start_game = self.client.recv(24)
        rooms[self.room]["status"] = "room locked temp"
        print("starting the game for room", self.room, "whose host is", self.username)

        #send_game_info_L = len(pickle.dumps(rooms[self.room]))

        # sending all the players a msg to start the game so our client side code knows to update the screen
        for player in rooms[self.room]["players list"]:
            print("sending to", player)
            room_player_objs[self.room]["players"][player].send(pickle.dumps("start game"))
            # send length of the game info , done as encounteru=ing eoferror on client side!
            #room_player_objs[self.room]["players"][player].send(bytes(str(send_game_info_L), 'utf-8'))
            room_player_objs[self.room]["players"][player].send(pickle.dumps(rooms[self.room]))
            #room_player_objs[self.room]["players"][player].send(pickle.dumps(("status","game started")))

        # as we are not sending the game info list to host so:
        #room_player_objs[self.room]["players"][self.username].send(pickle.dumps(rooms[self.room]))
        print("successfully sent msg to all the players")

        # there are three states of status - room locked, looking for players and game started (but room not locked)
        # for a room to be locked staus should be room locked else it will be looking for players or game started
        # in game started more
        # players can join the room in game started or in ooking for plaeyrs mode but no wwhen room is locked
        rooms[self.room]["status"] = "game started"

        # from now on player and host have to walk similar paths so we will run a function common to both
        # though host still gets some additional powers

        self.play_game()

        # run only after game ends or player leaves
        self.client.close()


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
                self.allocate_chance_num()
                self.new_player_dicto_update()
                print(self.username, "'s chance is", str(self.chance))
                print(rooms)
                # self.client.send(pickle.dumps(rooms[self.room]["players list"]))
                # send all the players the new list
                for player in rooms[self.room]["players list"]:
                    room_player_objs[self.room]["players"][player].send(pickle.dumps(rooms[self.room]["players list"]))

                self.play_game()


                # this will only be reached when player leaves or game ends
                self.client.close()

            #elif rooms[self.room]["status"] == "game started":
            # will be developed soon!

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

            # this is only while in developing stage as "game started" mode is not covered yet
            else:
                self.client.send(bytes("error",'utf-8'))
                self.client.close()

    def join_room(self):
        self.recv_room_num()


while True:
    client, addr = server.accept()
    print("Accepted connection from", addr)
    print("creating new thread for", addr)
    client_thread = threaded_Client(client, addr)
    client_thread.start()
    print("Looking for more clients in main thread")
    print(threading.enumerate())


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