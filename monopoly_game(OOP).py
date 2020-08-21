import tkinter as tk
from tkinter import ttk
import time,random
from grid_and_place_coordinates import *
from initialising_everything import *

chance = 0

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
        """
        frame = ask_screen(container, self)

        self.frames[ask_screen] = frame

        frame.grid(row=0, column=0, sticky="ew")

        self.show_frame(ask_screen)"""

        for F in (ask_screen,mono_board_display):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ask_screen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def enter_button_clicked(self,entry_wid, button_wid):
        global n_players
        n_players = int(entry_wid.get())
        self.n_players = n_players
        time.sleep(0.2)
        entry_wid.pack_forget()
        button_wid.pack_forget()

        if n_players > 8:
            n_players = 8

        if n_players < 2:
            n_players = 2

        for num in range(int(n_players)):
            tok = "token" + str(num+1)
            playing_tokens.append(tok)

        """c= 1
        for t in playing_tokens:
        chances.update({c:t})
        c+=1"""

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

class roll_dice(tk.Frame):

    def __init__(self,controller):
        self.controller = controller
        #self.chance = chance
        print("first chance-",chance)
        tk.Frame.__init__(self, controller)
        global roll_dice_d
        roll_dice_d = tk.Button(controller, text="Roll Dice!", bg="orange", command= lambda:self.virtual_dice())
        roll_dice_d.grid(row= 5, column=5)

    def virtual_dice(self):
        roll_dice_d.grid_forget()
        self.token_str = playing_tokens[chance]
        self.token_id = playing_token_id[chance]

        print(self.token_str, self.token_id)
        print(playing_token_id)
        print(playing_tokens)

        dice_roll = random.randint(1, 6)

        """show_dice = tk.StringVar()
        label_dice = "Dice Roll = " + str(dice_roll)
        show_dice.set(label_dice)"""

        position = master_dictionary[self.token_str]["position"]
        position+=dice_roll

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
        entry = ttk.Entry(self)
        entry.pack()
        enter_button = ttk.Button(self, text="Enter", command=lambda:controller.enter_button_clicked(entry, enter_button))
        enter_button.pack()
        play_button = ttk.Button(self, text="Play!", command=lambda:controller.show_frame(mono_board_display))
        play_button.pack()

class mono_board_display(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        controller.width-=320
        controller.height-=340
        controller.width=controller.width / 9
        controller.height = controller.height / 9


        # change names

        free_parking = tk.Frame(self, width=160, height=140, bg="orange", highlightbackground="black",
                                highlightthickness=1).grid(row=0, column=0)
        tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1).grid(row=0, column=1)
        tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1).grid(row=0, column=2)
        tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1).grid(row=0, column=3)
        tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1).grid(row=0, column=4)
        tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1).grid(row=0, column=5)
        tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1).grid(row=0, column=6)
        tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1).grid(row=0, column=7)
        tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1).grid(row=0, column=8)
        tk.Frame(self, width=controller.width, height=140, bg="LightSteelBlue1", highlightbackground="black",
                 highlightthickness=1).grid(row=0, column=9)
        go_jail = tk.Frame(self, width=160, height=140, bg="yellow", highlightbackground="black",
                           highlightthickness=1).grid(row=0, column=10)

        # left lane
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=1, column=0)
        tk.Frame(self, width=160, height=controller.height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=2, column=0)
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
        tk.Frame(self, width=controller.width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=1)
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
        tk.Frame(self, width=160, height=controller.height, bg="yellow", highlightbackground="black",

        highlightthickness = 1).grid(row=9, column=10)
        # self,controller, chance, token, token_str, player_str)

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
        print(chance)
        print("max chance-",max_chance)
        end_turn.grid_forget()
        roll_dice_d.grid(row=5, column=5)

class token:
    def __init__(self,token, token_str , player_str):
        self.token = token
        self.token_str = token_str
        self.player_str = player_str
            
    def my_special_init(self):
        self.dicto = {self.token_str:{"position":0, "row":row_coordinates["go_box"],"column":column_coordinates["go_box"]}}
        self.dicto_2 = {self.player_str:{"token_id":token,"token_str":self.token_str, "money":1500}}
        """master_dictionary[self.token_str] = {"position":0, "row":row_coordinates["go_box"],"column":column_coordinates["go_box"]}
        master_dictionary[self.player_str] = {"token_id":token,"token_str":self.token_str, "money":1500}"""
        master_dictionary.update(self.dicto)
        master_dictionary.update(self.dicto_2)
        self.token.grid(row=10,column=10)

    def token_move(self, position):
        #updating master dictionary
        master_dictionary[self.token_str]["position"] = position
        #position = master_dictionary[self.token_str]["position"]

        p = place_num[position]
        master_dictionary[self.token_str]["row"]  = row_coordinates[p]
        master_dictionary[self.token_str]["column"]=column_coordinates[p]

        row = master_dictionary[self.token_str]["row"]
        column = master_dictionary[self.token_str]["column"]
        self.token.grid_forget()
        self.token.grid(row=row, column=column)

game = Monopoly_Game()
game.mainloop()

#     def init_dictos(self,player_str, token_str,token):
#         master_dictionary["tokens"][token_str] = {}
#         master_dictionary["players"][player_str] = {}
# token_str = ('token1','token2','token3','token4','token5','token6','token7','token8')
# master_dictionary["tokens"][token_str[token]] = {"row":row_coordinates["go_box"], "column": column_coordinates["go_box"]}
# row = row_coordinates[place_num[position_on_board]]
# column = column_coordinates[place_num[position_on_board]]
#         token_tuple = (token1,token2,token3,token4,token5,token6,token7,token8)
#         token_str = ('token1','token2','token3','token4','token5','token6','token7','token8')
#         player_str = ('player1','player2','player3','player4','player5','player6','player7','player8')
#     """      for token in range(n_players):
#             master_dictionary["tokens"][token_str[token]] = {"position": 0, "row": row_coordinates['go_box'],"column": column_coordinates['go_box'],"token_id":token_tuple[token]}
#             master_dictionary["players"][player_str[token]] = {"token": token_tuple[token], "money": 1500}
#             token_tuple[token].grid(row=10, column=10)"""
# row=master_dictionary["tokens"][token_str]["row"],column=master_dictionary["tokens"][token_str]["column"]