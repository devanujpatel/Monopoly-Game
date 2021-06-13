import tkinter as tk
from tkinter import ttk
import time,random
from game_coords import *
from initialising_everything import *

chance = 0
sticky_id = {"token1":"N","token2":"S","token3":"w","token4":"e","token5":"NE","token6":"NW","token7":"SW","token8":"se"}
# TODO:
#   make names of places on board
#   update readme
#   add comments in the code
#   collaborate with property class
#   color code
#   show status
#   error handling (in n_players entry)

class Monopoly_Game(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.width = container.winfo_screenwidth()  # width of screen
        self.height = container.winfo_screenheight()  # height of screen

        container.winfo_toplevel().geometry("%dx%d%+d%+d" % (self.width, self.height, 0, 0))

        self.frames = {}

        for F in (ask_screen,mono_board_display):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ask_screen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def enter_button_clicked(self,entry_wid):
        global n_players
        n_players = int(entry_wid.get())
        self.n_players = n_players
        time.sleep(0.2)
        entry_wid.pack_forget()

        if n_players > 8:
            n_players = 8

        if n_players < 2:
            n_players = 2

        for num in range(int(n_players)):
            tok = "token" + str(num+1)
            playing_tokens.append(tok)

        t1 = token(token1, "token1", "player1")
        t2 = token(token2, "token2", "player2")
        t3 = token(token3, "token3", "player3")
        t4 = token(token4, "token4", "player4")
        t5 = token(token5, "token5", "player5")
        t6 = token(token6, "token6", "player6")
        t7 = token(token7, "token7", "player7")
        t8 = token(token8, "token8", "player8")

        t1.my_special_init()
        t2.my_special_init()

        if "token3" in playing_tokens:
            t3.my_special_init()

        if "token4" in playing_tokens:
            t4.my_special_init()

        if "token5" in playing_tokens:
            t5.my_special_init()

        if "token6" in playing_tokens:
            t6.my_special_init()

        if "token7" in playing_tokens:
            t7.my_special_init()

        if "token8" in playing_tokens:
            t8.my_special_init()

        token_objs = [t1, t2, t3 , t4, t5, t6, t7, t8]

        for i in range(n_players):
            playing_token_id.append(token_objs[i])

        global sticky_id


        """        x = 0.1
        y = 0.1
        for T in playing_tokens:
            if x == 0.30000000000000004:
                x = 0.3
            relx.update({T:x})
            rely.update({T:y})
            x+=0.2
            if x ==0.8999999999999999:
                x = 0.1
                y = 0.7
        print(relx,rely)"""

class roll_dice(tk.Frame):

    def __init__(self,controller):
        self.controller = controller
        tk.Frame.__init__(self, controller)

        global roll_dice_d
        roll_dice_d = tk.Button(controller, text="Roll Dice!", bg="orange", command= lambda:self.virtual_dice())
        roll_dice_d.grid(row= 5, column=5)

    def virtual_dice(self):
        roll_dice_d.grid_forget()
        self.token_str = playing_tokens[chance]
        self.token_id = playing_token_id[chance]

        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        dice_roll = dice_roll1 + dice_roll2
        show_dice = tk.StringVar()
        label_dice = "Dice Roll = " + str(dice_roll)
        show_dice.set(label_dice)
        tk.Label(self.controller, textvariable=show_dice, bg="green", fg="orange", width=12, height=2).grid(row=7,column=5)

        position = master_dictionary[self.token_str]["position"]

        place = place_num[position]

        position += dice_roll

        if position >= 40:
            position -= 40

        new_position = position
        self.token_id.token_move(new_position)

        global end_turn
        end_turn = ttk.Button(self.controller, text="End Turn!", command = lambda:self.controller.end_turn_clicked())
        end_turn.grid(row=6,column=6)

class ask_screen(tk.Frame):
    def __init__(self, parent, controller):
        global entry,enter_button
        tk.Frame.__init__(self,parent)
        self.controller = controller
        entry = ttk.Entry(self)
        entry.pack()
        play_button = ttk.Button(self, text="Play!", command=lambda:self.play_but_clicked())
        play_button.pack()

    def play_but_clicked(self):
        self.controller.enter_button_clicked(entry)
        self.controller.show_frame(mono_board_display)

class mono_board_display(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        controller.width-=320
        controller.height-=350
        controller.width = controller.width / 9
        controller.height = controller.height / 9
        self.height = controller.height
        self.width = controller.width
        # (self, property_id, property_str, row, column, buying_price, rent, house_price, one_house_rent, color_group)
        """Atlantic Avenue
        B & O Railroad
        Baltic Avenue
        Boardwalk
        Connecticut Avenue
        Electric Company
        Illinois Avenue
        Indiana Avenue
        Kentucky Avenue
        Marvin Gardens
        Mediterranean Avenue
        New York Avenue
        North Carolina Avenue
        Oriental Avenue
        Pacific Avenue
        Park Place
        Pennsylvania Avenue
        Pennsylvania Railroad
        Reading Railroad
        Short Line
        St. Charles Place
        St. James Place
        States Avenue
        Tennessee Avenue
        Ventnor Avenue
        Vermont Avenue
        Virginia Avenue
        Water Works"""

        free_parking = tk.Frame(self, width=160, height=140, bg="orange", highlightbackground="black",
                                highlightthickness=1)
        free_parking_obj = property(free_parking, "free_parking", 0,0)
        
        kentucky_avenue = tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1)
        kentucky_avenue_obj = property(kentucky_avenue, "kentucky_avenue", 0,1)
        
        chance2 = tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1)
        chance2_obj = property(chance2, "chance2", 0,2)

        indiana_avenue = tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1)
        indiana_avenue_obj = property(indiana_avenue, "indiana_avenue", 0,3)

        illinois_avenue = tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1)
        illinois_avenue_obj = property(illinois_avenue, "illinois_avenue", 0,4)

        b_and_o_railroad = tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1)
        b_and_o_railroad_obj = property(b_and_o_railroad, "b_and_o_railroad", 0,5)

        atlantic_avenue = tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1)
        atlantic_avenue_obj = property(atlantic_avenue, "atlantic_avenue", 0,6)

        ventnor_avenue = tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1)
        ventnor_avenue_obj = property(ventnor_avenue, "ventnor_avenue", 0,7)

        water_works = tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1)
        water_works_obj = property(water_works, "water_works", 0,8)

        marvin_garden = tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1)
        marvin_garden_obj = property(marvin_garden, "marvin_garden", 0,9)

        go_to_jail = tk.Frame(self, width=160, height=140, bg="yellow", highlightbackground="black",
                           highlightthickness=1)
        go_to_jail_obj = property(go_to_jail, "go_to_jail", 0,10)

        # left lane
        new_york_avenue = tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1)
        new_york_avenue_obj = property(new_york_avenue, "pacific_avenue", 1,0)

        tennessee_avenue = tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1)
        tennessee_avenue_obj = property(tennessee_avenue, "tennessee_avenue", 2,0)

        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=3, column=0)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=4, column=0)
        tk.Frame(self, width=160, height=controller.height, bg='green', highlightbackground="black",
                 highlightthickness=1).grid(row=5, column=0)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=6, column=0)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=7, column=0)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=8, column=0)
        tk.Frame(self, width=160, height=controller.height, bg="yellow", highlightbackground="black",
                 highlightthickness=1).grid(row=9, column=0)

        # lower lane
        just = tk.Frame(self, width=160, height=140, bg="pink", highlightbackground="black",
                        highlightthickness=1).grid(row=10, column=0)
        place3= tk.Frame(self, width=controller.width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1)
        place3.grid(row=10, column=1)
        tk.Frame(self, width=controller.width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=2)
        tk.Frame(self, width=controller.width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=3)
        tk.Frame(self, width=controller.width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=4)
        tk.Frame(self, width=controller.width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=5)
        tk.Frame(self, width=controller.width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=6)
        tk.Frame(self, width=controller.width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=7)
        tk.Frame(self, width=controller.width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=8)
        tk.Frame(self, width=controller.width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=9)
        go_box = tk.Frame(self, width=160, height=140, bg="brown", highlightbackground="black",
                          highlightthickness=1)
        go_box.grid(row=10, column=10)

        # right lane
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=1, column=10)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=2, column=10)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=3, column=10)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=4, column=10)
        tk.Frame(self, width=160, height=controller.height, bg='green', highlightbackground="black",
                 highlightthickness=1).grid(row=5, column=10)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=6, column=10)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=7, column=10)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=8, column=10)
        place= tk.Frame(self, width=160, height=controller.height, bg="yellow", highlightbackground="black",
                 highlightthickness = 1)
        place.grid(row=9, column=10)
        """

        place1 = tk.Label(place, bg="orange", width=2, height=1)
        place1.place(relx=0.3, rely=0.7)

        place2 = tk.Label(place, bg="orange", width=2, height=1)
        place2.place(relx=0.1, rely=0.7)

        place3 = tk.Label(place, bg="orange", width=2, height=1)
        place3.place(relx=0.5, rely=0.7)

        place2 = tk.Label(place, bg="blue", width=2, height=1)
        place2.place(relx=0.7, rely=0.7)

        place3 = tk.Label(place, bg="blue", width=2, height=1)
        place3.place(relx=0.5, rely=0.1)

        place1 = tk.Label(place, bg="light green", width=2, height=1)
        place1.place(relx=0.3, rely=0.1)

        place2 = tk.Label(place, bg="light green", width=2, height=1)
        place2.place(relx=0.1, rely=0.1)

        place3 = tk.Label(place, bg="light green", width=2, height=1)
        place3.place(relx=0.7, rely=0.1)"""

        global token1, token2, token3, token4, token5, token6, token7, token8

        token1 = tk.Label(self, text="T1", width=2, height=1)
        token2 = tk.Label(self, text="T2", width=2, height=1)
        token3 = tk.Label(self, text="T3", width=2, height=1)
        token4 = tk.Label(self, text="T4", width=2, height=1)
        token5 = tk.Label(self, text="T5", width=2, height=1)
        token6 = tk.Label(self, text="T6", width=2, height=1)
        token7 = tk.Label(self, text="T7", width=2, height=1)
        token8 = tk.Label(self, text="T8", width=2, height=1)

        global dice
        dice = roll_dice(self)

    def end_turn_clicked(self):

        global chance

        chance += 1
        max_chance = n_players

        if max_chance == chance:
            chance = 0

        end_turn.grid_forget()
        roll_dice_d.grid(row=5, column=5)

class token:
    def __init__(self,token, token_str , player_str):
        self.token = token
        self.token_str = token_str
        self.player_str = player_str
            
    def my_special_init(self):
        global sticky_id
        self.dicto = {self.token_str:{"position":0, "row":row_coordinates["go_box"],"column":column_coordinates["go_box"]}}
        self.dicto_2 = {self.player_str:{"token_id":token,"token_str":self.token_str, "money":1500}}
        master_dictionary.update(self.dicto)
        master_dictionary.update(self.dicto_2)
        self.token.grid(row=10,column=10, sticky = sticky_id[self.token_str])

    def token_move(self, position):

        master_dictionary[self.token_str]["position"] = position
        p = place_num[position]

        row = row_coordinates[p]
        column = column_coordinates[p]
        self.token.grid_forget()
        self.token.grid(row=row, column=column, sticky=sticky_id[self.token_str])

class property:
    def __init__(self, property_id, property_str, row, column):
        #, buying_price, rent, house_price, one_house_rent, group)

        property_id.grid(row=row, column=column)
        properties.update({property_str:{"property_id":property_id}})
                          #, "rent":rent,buying price
        #                                "house_price":house_price, "one_house_rent":one_house_rent, "color_group":group}
        
            

game = Monopoly_Game()
game.mainloop()

"""## flow of the game

### ask frame

### displaying our board

### moving multiple tokens"""
