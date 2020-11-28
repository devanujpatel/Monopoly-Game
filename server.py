import pickle
import socket
import threading
import time

# create a af_inet streaming server
server = socket.socket()
server.bind(("", 9999))
server.listen()

# a dictionary that contains each and every room created and its data about players
rooms = {}
# a dictionary which will contain information which is sent to client many times during the course of the game
room_game_info = {}
# a dicto which will contain socket objects of each and every player in a particular room
room_player_objs = {}
# for holding token directions of a room
token_dir = {}
# contains all the existing rooms as the name suggests
existing_rooms = []
# start making rooms with no. 100
room = 100

# the below dictionaries are for sending the room num info to clients who want to join a room

# clients whom we need to send existing room numbers
send_room_num_clients = []
# a list to contain all info to be sent to client in send_room_num_clients
send_room_info_list = {}


def send_room_nums():
    if len(send_room_num_clients) != 0:
        send_item = []

        if len(send_room_info_list) != 0:
            for r in send_room_info_list.values():
                send_item.append(r)

            for client in send_room_num_clients:
                try:
                    client.send(pickle.dumps(send_item))
                except ConnectionError:
                    send_room_num_clients.remove(client)
    else:
        # do nothing if we have no one to send
        # this type of call is made when the dictionaries update
        # note that this type of call cannot be called when a new client joins
        pass


class threaded_Client(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr

    def run(self):
        global rooms, room
        # wait for client to send whether he/she wants to join a room or create a room
        try:
            self.what_to_do = self.client.recv(1024)

            if self.what_to_do:
                self.what_to_do = pickle.loads(self.what_to_do)

            # create a room
            if self.what_to_do == "create room":
                self.create_room()

            # join a room
            if self.what_to_do == "join room":
                self.join_room()

        except ConnectionError as ce:
            print(ce, self.addr, "left")
            self.client.close()

    def disband_room(self):
        pass

    def create_room(self):
        global rooms, room
        # give our host player a room no.
        self.room = room
        # add the particular room no. in existing rooms list to later know that the room exists
        existing_rooms.append(self.room)

        # increment for any other player who creates a new room as we want to give new room num to each room created
        room += 1

        # recv username from the player for that particular game
        # later a save game feature will be available and
        # the player might have to choose who he/she is from the saved room
        self.ask_and_verify_username()

        if self.username == "":
            # nothing to do host left , room disbanded then also do nothing as no dictionary has been
            # updated for the room
            self.client.close()
            existing_rooms.remove(self.room)

        else:
            # do not disband room

            # the rooms dicto will be updated with a room no. and other necessary information the game info key is the
            # main key in which the game data will be stored and sent to all the clients at the start of the game after
            # which the server and all the clients will maintain it according to the instructions sent
            rooms.update(
                {self.room: {"host": self.username, "status": "looking for players", "color responses": [0, [], {}],
                             "players list": [], "chance alloc num": 0, "player chances": {}, "game info": {},
                             "inverted chances": {},
                             "chance": 0, "rounds completed": 0, "token dir": {}, "send flag": True, "trade flag": True}})

            # for storing and then allocating different poistions to players to avoid overlapping of tokens (these are
            # sticky options of tkinter)
            token_dir.update({self.room: ["N", "S", "E", "W", "NE", "SE", "NW", "SW"]})
            # contains the client objects of particular room
            room_player_objs.update({self.room: {}})

            # the names are self explanatory
            self.allocate_chance_num()
            self.new_player_dicto_update()

            # send our host the players in his room (at the moment;it would be only one player i.e the host itself)
            try:
                self.client.send(pickle.dumps(rooms[self.room]["players list"]))

                # now that the room is properly established we can send it to our clients
                send_room_info_list.update({self.room: [self.room, self.username, 1]})
                send_room_nums()
                self.start_game = pickle.loads(self.client.recv(1024))

                # useful for setting timeout during gameplay
                rooms[self.room].update({"responded": {}})
                for player in rooms[self.room]["players list"]:
                    rooms[self.room]["responded"].update({player: False})

                rooms[self.room]["status"] = "room locked temp"
                rooms[self.room].update({"start game count": 0})

                # when recved by client he/she starts to recv things sent further after, this is a type of signal
                self.client.send(pickle.dumps("start game"))
                # send data holder
                room_player_objs[self.room][self.username].send(pickle.dumps(rooms[self.room]))
                print("sent")
                # just keeping a track of players
                rooms[self.room]["start game count"] += 1

                if rooms[self.room]["start game count"] == len(rooms[self.room]["players list"]):
                    rooms[self.room]["status"] = "game started"
                else:
                    pass

                # play game...
                self.color_updates()

            except ConnectionError:
                # host left so disband the room
                del rooms[self.room]
                existing_rooms.remove(self.room)

                # disband room, send other players the same
                # ---------------------------------------
                self.client.close()



            """if self.go_ahead == True:

                # recv a msg to know that host wants to start the game -- recall blocking sockets
                try:
                    self.start_game = pickle.loads(self.client.recv(1024))

                    # useful for setting timeout during gameplay
                    rooms[self.room].update({"responded": {}})
                    for player in rooms[self.room]["players list"]:
                        rooms[self.room]["responded"].update({player: False})

                    rooms[self.room]["status"] = "room locked temp"
                    rooms[self.room].update({"start game count": 0})

                    # when recved by client he/she starts to recv things sent further after, this is a type of signal
                    self.client.send(pickle.dumps("start game"))
                    # send data holder
                    room_player_objs[self.room][self.username].send(pickle.dumps(rooms[self.room]))
                    print("sent")
                    # just keeping a track of players
                    rooms[self.room]["start game count"] += 1

                    if rooms[self.room]["start game count"] == len(rooms[self.room]["players list"]):
                        rooms[self.room]["status"] = "game started"
                    else:
                        pass

                    # play game...
                    self.color_updates()
                    

                except ConnectionError:
                    print("room disbanded")
                    del rooms[self.room]

            else:
                # the room would be disbanded
                pass"""

    def join_room(self):
        send_room_num_clients.append(self.client)
        send_room_nums()
        self.recv_room_num()

    def recv_room_num(self):
        self.room = pickle.loads(self.client.recv(1024))
        self.room = int(self.room)
        send_room_num_clients.remove(self.client)
        self.check_recved_room_num()

        # there are three states of status - room locked, looking for players and game started for a room to be
        # locked status should be room locked ,either the game has starteed or not in this state no more players will
        # be able to join else it will be-looking for players or game started players can join the room in game
        # started or in looking for players mode but no when room is locked

    def ask_and_verify_username(self):
        while True:
            try:
                self.username = self.client.recv(1024)

                if self.username:
                    self.username = pickle.loads(self.username)

                if self.what_to_do == "join room":

                    if self.username in rooms[self.room]['players list']:
                        self.client.send(pickle.dumps("occupied username"))
                        # again try to recv a username and validate again

                    else:
                        # means nothing to server except it goes in the else and it moves on
                        self.client.send(pickle.dumps("go ahead"))
                        break

                else:
                    # means nothing to server except it goes in the else and it moves on
                    self.client.send(pickle.dumps("go ahead"))
                    break

            except ConnectionError as ce:
                if self.what_to_do == "create room":
                    print(ce, self.addr, "left , he was a host so room disbanded")
                    # means disband room or leave room handled by the method which calls it
                    self.username = ""
                    break

                else:
                    self.username = ""
                    break

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

        # inverted chance is chance = whose chance it is
        rooms[self.room]["inverted chances"].update({self.chance: self.username})

        # add him in players list
        rooms[self.room]["players list"].append(self.username)

        # in the objects dcto also which was created by the host
        room_player_objs[self.room].update({self.username: self.client})

        # for avoiding token overlapping as discussed earlier
        rooms[self.room]["token dir"].update({self.username: token_dir[self.room].pop(-1)})

    def check_recved_room_num(self):
        if self.room not in existing_rooms:
            # if room doesnt exist then notify the client about the same
            self.client.send(pickle.dumps("room doesn't exist"))
            # again wait for client to send room num
            self.recv_room_num()

        elif self.room in existing_rooms:

            if rooms[self.room]["status"] == "looking for players":
                print("joined")
                time.sleep(0.5)
                self.client.send(pickle.dumps("joined successfully"))

                self.ask_and_verify_username()

                self.allocate_chance_num()
                self.new_player_dicto_update()

                # send all the players the new players list
                for player in rooms[self.room]["players list"]:
                    room_player_objs[self.room][player].send(pickle.dumps(rooms[self.room]["players list"]))

                send_room_info_list[self.room][2] = len(rooms[self.room]["players list"])
                send_room_nums()

                # then check in a while true loop  for status - room locked temp(rlt) cuz when host starts the game
                # the stat is changed to rlt
                while True:
                    time.sleep(0.6)
                    if rooms[self.room]["status"] == "room locked temp":

                        break

                    else:
                        time.sleep(0.6)
                # runs only after stat is rlt
                room_player_objs[self.room][self.username].send(pickle.dumps("start game"))
                room_player_objs[self.room][self.username].send(pickle.dumps(rooms[self.room]))

                rooms[self.room]["start game count"] += 1

                if rooms[self.room]["start game count"] == len(rooms[self.room]["players list"]):
                    rooms[self.room]["status"] = "game started"

                self.color_updates()


            # todo:
            #   elif rooms[self.room]["status"] == "game started":
            #   will be developed soon!

            elif rooms[self.room]["status"] == "room locked temp":
                # send the client that room is locked locking the room is in the hands of the host but when the host
                # starts the actual game then for some seconds the room will be locked(room locked temp) then again
                # it will be unlocked as it is the default though the host can lock it later the room was locked
                # temporarily as the client side code can only recv one thing at a time and it would already be
                # looking for new pltheayers list incase someone new joins whenever someone new joins the new comer
                # sends all the other players the new updated players list but when the host starts the game all the
                # clients need to recv the msg so the room is locked temporarily so that no new player can join the
                # room and send the new players list when the host is trying to start the game ----- this is a
                # precautionary measure this is to handle a situation where the starting of game command from the
                # host and joining of a new player doesn't collide so that the client code do not gets confused what
                # it has to recv and also the client side thread on the server gets to know what is happening
                self.client.send(bytes("unable to join temp"))
                # the client side code will then inform our client to try entering the room after a few seconds
                self.recv_room_num()
                # new idea here - do a while loop so that the player joins automatically when the room is again unlocked
                # thus our client doesn't have to send to join room again
            elif rooms[self.room]["status"] == "room locked":
                self.client.send(pickle.dumps("room locked"))
                self.recv_room_num()

            # this is only while in developing stage as "game started" mode is not covered yet
            else:
                self.client.send(pickle.dumps("error"))
                self.client.close()

    def re_allocate_chance(self):
        rooms[self.room]["player chances"] = {}
        rooms[self.room]["inverted chances"] = {}
        rooms[self.room]["chance alloc num"] = 0
        for player in rooms[self.room]["players list"]:
            rooms[self.room]["player chances"].update({player: rooms[self.room]["chance alloc num"]})
            rooms[self.room]["chance alloc num"] += 1

        for k, v in rooms[self.room]["player chances"]:
            rooms[self.room]["inverted chances"].update({v: k})

    def color_updates(self):

        # send flag = True means u are good to go and send flag False means wait for sometime and then send when
        # send flag is True

        # first of all we get the favourite color of each player
        rooms[self.room]["color responses"][2].update({self.username: "not ready"})
        self.fav_color = pickle.loads(self.client.recv(1024))
        rooms[self.room]["color responses"][2].update({self.username: "ready"})

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

        # send the leftover players the color
        while True:
            time.sleep(1)

            if len(self.not_reachable) == 0:
                break

            for player in self.not_reachable:
                if rooms[self.room]["color responses"][2][player] == "ready":
                    room_player_objs[self.room][player].send(pickle.dumps(self.fav_color))
                    self.sent.append(player)
                    self.not_reachable.remove(player)

        # after this we start the actual game!
        self.no_response = 0
        # self.responded = False
        self.rent_given = True
        # running this will then run main_game
        self.assess_situation()

    def main_game(self):

        # a client conn only gets closed when he/she leaves
        # when while loop (2) gets over their is a doubt whether the client is disconnected
        # so when the main while loop(1) ends the conn will get over

        # when the player leaves many things can be done- stop game , continue or forget the left player

        # can make a option to save and leave game when one player leaves ,to the host if host decides to continue
        # the game then the player will be erased (new option on the way) elif host decides to save the game then the
        # game will end, inference drawn, and saved too(of course) host can simply just end the game also it is to be
        # decided how to manage the game after the removal of the player (as we can allow to let the player join
        # again) if host leaves the whole game is disbanded and option to save the game goes to player 1

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
                print(rooms[self.room]["chance"], rooms[self.room]["player chances"][self.username],
                      rooms[self.room]["responded"][self.username], self.username)

                if rooms[self.room]["chance"] == rooms[self.room]["player chances"][self.username] and \
                        rooms[self.room]["responded"][self.username] == False:

                    self.client.settimeout(30)
                    print("timeout set", self.username)

                while True:
                    try:
                        self.data_tup = self.client.recv(1048)
                        break
                    except socket.timeout:
                        print("timed out",self.username)
                        if rooms[self.room]["responded"][self.username] == False:
                            self.no_response += 1
                            print("I missed chance", self.username, "responses- ", self.no_response)

                            if self.no_response == 3:
                                print("checking if active...")
                                return "check if active"

                            else:
                                self.data_tup = (self.username, "chance missed")
                                print(self.username, "missed chance", self.no_response)
                                self.client.settimeout(None)
                                print("timeout removed", self.username)
                                self.end_turn()
                                self.data_tup = None
                                # if data tup is none then the elif statements will catch it and pass so that new cycle
                                # of while loop starts
                                break

                        else:
                            if self.rent_given == False:
                                print("RP", self.rent_proposal, self.username)
                                self.money_to_be_sub = int(2 * self.rent_proposal[2])
                                # send the updates first
                                self.send_updates((self.rent_proposal[0], "money",
                                                   rooms[self.room]["game info"][self.rent_proposal[0]][
                                                       "money"] - self.money_to_be_sub),
                                                  rooms[self.room]["players list"])
                                time.sleep(2)
                                self.send_updates((self.rent_proposal[1], "money",
                                                   rooms[self.room]["game info"][self.rent_proposal[1]][
                                                       "money"] + self.money_to_be_sub),
                                                  rooms[self.room]["players list"])
                                # then update server side dicto also
                                rooms[self.room]["game info"][self.rent_proposal[0]]["money"] -= self.money_to_be_sub
                                rooms[self.room]["game info"][self.rent_proposal[1]]["money"] += self.money_to_be_sub
                                self.rent_given = True

                                # todo:
                                #   what if at any moment money to be paid less then money in hand

                    except ConnectionError:
                        print("conn error")
                        print("player left", self.username, self.room)
                        # give loop(2) chance to assess the situation then if client has to leave then break from main loop too
                        # if not then continue to run loop(1) which will then run loop(2)
                        return "check if active"

                if self.data_tup:
                    self.data_tup = pickle.loads(self.data_tup)
                    print(self.data_tup)
                    self.client.settimeout(None)
                    print("timeout removed", self.username)
                else:
                    self.data_tup = None

            # meant for checking connection error but not specifically coded
            # check if some error is coming through the print statement
            except Exception as e:
                print(e)
                print("player left", self.username, self.room)
                # give loop(2) chance to assess the situation then if client has to leave then break from main loop too
                # if not then continue to run loop(1) which will then run loop(2)
                return "check if active"

            # if it is to end our turn then do so; sent only when 30 sec timeout happens or end turn btn clicked on
            if self.data_tup == ("end my turn"):
                self.end_turn()

            elif self.data_tup == None:
                pass

            elif self.data_tup[-1] == "rent":
                self.client.settimeout(150)
                self.rent_proposal = self.data_tup
                self.rent_given = False

            elif self.data_tup[1] == "paying rent":
                self.rent_given = True
                self.client.settimeout(None)

            elif self.data_tup[1] == "coudn't buy":  # todo:
                self.send_updates(self.data_tup, rooms[self.room]["players list"])  # client side for coudnt buy

            elif self.data_tup[1] == "trade proposal":
                if rooms[self.room]["trade flag"] == True:
                    rooms[self.room]["trade flag"] = False
                    self.send_updates(self.data_tup, rooms[self.room]["players list"])
                else:
                    self.send_updates_to_specific_person(self.username, ("cant trade"))

            elif self.data_tup[1] == "trade finalised":
                rooms[self.room]["trade flag"] = True
                self.send_updates(self.data_tup, rooms[self.room]["players list"])

            elif self.data_tup[1] == "trade declined":
                rooms[self.room]["trade flag"] = True
                self.send_updates(self.data_tup, rooms[self.room]["players list"])

            # player leaves gracefully!
            elif self.data_tup[0] == "leave" and self.data_tup[1] == "player":
                # leave_confirmation_status = "ask again player"
                return "ask again player"

            elif self.data_tup[0] == "leave" and self.data_tup[1] == "host":
                # leave_confirmation_status = "ask again host"
                return "ask again host"

            # host sends to end game
            elif self.data_tup[0] == "end game" and self.data_tup[1] == "host":
                # leave_confirmation_status = "ask to save"
                return "ask to save"

            # elif self.data_tup[0] == "round" and self.data_tup[1] == "completed":
            #    self.responded = False
            #    print("in [1] and [2]")

            # elif self.data_tup[0] == "RC":
            #    print("got rc", self.username)
            #    self.responded = False

            elif self.data_tup[1] == "position":
                rooms[self.room]["responded"][self.username] = True
                self.munch_data()

            else:
                # LET'S MUNCH DOWN OUR DATA
                self.munch_data()

    def munch_data(self):
        print(self.data_tup, "= data tup")

        if len(self.data_tup) == 3:
            rooms[self.room]["game info"][self.data_tup[0]][self.data_tup[1]] = self.data_tup[2]
        elif len(self.data_tup) == 2:
            rooms[self.room][self.data_tup[0]] = self.data_tup[1]
        elif len(self.data_tup) == 4:
            if self.data_tup[2] == "update" and self.data_tup[1] == "properties":
                # means we have to add something o the dicto about properties
                rooms[self.room]["game info"][self.data_tup[0]][self.data_tup[1]].update({self.data_tup[3]: {
                    "status": "normal", "houses": 0, }})

        else:
            pass
        # send the same to others.
        self.send_updates(self.data_tup, rooms[self.room]["players list"])

    def send_updates_to_specific_person(self, player_name, update):
        while True:
            if rooms[self.room]["send flag"] is True:
                rooms[self.room]["send flag"] = False
                room_player_objs[self.room][player_name].send(pickle.dumps(update))
                rooms[self.room]["send flag"] = True
                break
            else:
                time.sleep(0.2)

    def send_updates(self, data_tup, players_to_be_sent):
        # false means don't send and true means send
        # players_left = players_to_be_sent
        # sent_players = []
        # error_players = []
        while True:
            # time.sleep(0.2)
            if rooms[self.room]["send flag"] is True:
                rooms[self.room]["send flag"] = False
                data_tup = pickle.dumps(data_tup)
                for player in players_to_be_sent:
                    time.sleep(0.3)
                    print("sending data tup", pickle.loads(data_tup), "to", player, self.username)
                    try:
                        room_player_objs[self.room][player].send(data_tup)
                        # players_left.remove(player)
                        # sent_players.append(player)
                    except ConnectionResetError or ConnectionError:
                        # error_players.append(player)
                        self.r = self.player_left_protocol(player)

                        if self.r[0] == "end all":
                            pass

                        elif self.r[0] == "cont":
                            room_player_objs[self.r[1][0]].send_updates(data_tup, self.r[1])

                        else:
                            pass

                rooms[self.room]["send flag"] = True
                break
            else:
                time.sleep(0.2)

    def assess_situation(self):

        # this is while True no. (1)
        while True:

            # constantly run the loop(2) to play game then the main_game fnc will return for situation handling
            lcs = self.main_game()

            # assess the situation possible situations: 1> CLIENT LEAVES GRACEFULLY 2> CLIENT GETS DISCONNECTED (
            # doubt if player is active) 3> HOST ENDS THE GAME 4> HOST LEAVES ABRUPTLY situation 1 : make the player
            # leave but keep his dicto alive, ->then ask host if he wants to still continue the game if yes then
            # erase the player dicto and distribute props to bank and if no then ask host to save the game sit 2,
            # the player will be asked if he/she is still in the game with a timeout of 20 seconds if timeout happens
            # then proceed as situation 1 after '->' situation 3 : ask host to save game situation 4 : ask player1
            # the option to end and save game

            print(lcs)
            # lcs = leave_confirmation_status and wtd = what_to_do
            if lcs == "check if active":
                wtd = self.player_left_protocol(self.username)
            if lcs == "ask again host":
                wtd = self.confirm_leave("host")
            if lcs == "ask again player":
                wtd = self.confirm_leave("player")
            if lcs == "ask to save":
                wtd = self.end_game_confirm()

            # more lcs on the way

        # ACC TO WTD(what to do) REACT FURTHER (like run a fnc) AND THEN AFTER THAT RESPECTIVE FNC has completed
        # execution REACT ACC. TO THE NEW WTD I.E PROBABLY BREAK OR RUN MAIN_GAME_AGAIN WHICH MEANS TO JUST CONTINUE
        # THE LOOP OF GAME AS USUAL

    # still left to do, associated with the main game and play game functions

    def end_turn(self):
        rooms[self.room]["responded"][self.username] = True
        # increase chance num by one
        rooms[self.room]["chance"] += 1
        # while increasing chance we also need to see if chance number is within limit
        if rooms[self.room]["chance"] == len(rooms[self.room]["players list"]):
            # set everyone's responded to False
            # send client this update then client will send the server will recv it to set everyone's responded to False
            # RC for round completed
            # self.send_updates(("RC"))
            for player in rooms[self.room]["players list"]:
                rooms[self.room]["responded"][player] = False

            rooms[self.room]["rounds completed"] += 1
            rooms[self.room]["chance"] = 0

        # send all our clients the update
        self.send_updates(("chance", rooms[self.room]["chance"]), rooms[self.room]["players list"])
        self.send_updates(("rounds completed", rooms[self.room]["rounds completed"]), rooms[self.room]["players list"])
        # send to end turn so client can check if he has to show dice btn
        # do not do this before the above updates as then chance will not be updated and same chance will be carried on
        if self.data_tup[1] != "chance missed":
            self.send_updates(("end my turn"), rooms[self.room]["players list"])
        else:
            self.send_updates(("chance missed"), rooms[self.room]["players list"])

    def confirm_leave(self, player_desig):
        # return a value ; active or not , if host not active then ask player1
        # if player not active then ask host his options
        pass

    def player_left_protocol(self, player):
        del rooms[self.room]["token dir"][player]
        rooms[self.room]["players list"].remove(player)
        del room_player_objs[self.room][player]

        if player == rooms[self.room]["host"]:
            for player in rooms[self.room]["players list"]:
                room_player_objs[self.room][player].send(pickle.dumps("kill it all"))
                room_player_objs[self.room][player].close()

            del rooms[self.room]
            return "end all"

        if len(rooms[self.room]["players list"]) == 1:
            for conn in room_player_objs:
                conn.send(pickle.dumps("kill it all"))
                conn.close()
            del rooms[self.room]
            return "end all"

        else:
            del rooms[self.room]["game info"][player]
            rooms[self.room]["players list"].remove(player)
            self.re_allocate_chance()
            # le the client know that remove a player
            room_player_objs[self.room][rooms[self.room]["host"]].send(
                pickle.dumps(("conn error", player, rooms[self.room])))
            return "cont"

    def save_room(self):
        pass

    def end_game_confirm(self):
        # it is ; ask to save room or end game now
        pass

    def close_conn(self, conn):
        conn.close()

    def read_saved_game(self):
        pass

    def waiting_mode(self):
        pass


while True:
    client, addr = server.accept()
    client_thread = threaded_Client(client, addr)
    client_thread.start()

# TODO
#   give timeouts so that you can reomove a person who is inactive for a long time like 120 seconds or 3 times inactive for 30 sec
#   improve gui looks
#   verify username (is it pre occupied or client sent an empty string,etc...)
#   handle input erros from client side like client sent a str instead of room int
#   dont allow to start game if only host is in the room and also automatically start game when 8 players join
#   see the check recved room num comments for ndew features update   (3)
#   also make a backup feature in the game (players can take backup at regular intervals)
#   think of a way to let player join again with same game status as before
#
#   see below comments and resolve them and also see keep for the doubts

# ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
# what happens when server sends something but the client didnt recv it as the client has lost connection
# when u send the length of msg using the HEADER technique then recv whole msg then we use recv two times one time
# on recver side but send once on the sender side????


# DONE
# ask layer to chooose color agian if he she doesnt choose one
#
# '#fd7e00'
