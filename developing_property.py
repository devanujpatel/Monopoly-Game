import tkinter as tk
#from tkinter import ttk
import tkinter.font as font
import time, random
from grid_and_place_coordinates import *
from initialising_everything import *

#------------------------------ ☺☺☻☻ PLEASE IGNORE ALL THE DOC-STRINGS! ☺☺☻☻-------------------------



container = tk.Tk()
width = container.winfo_screenwidth()  # width of screen
height = container.winfo_screenheight()  # height of screen

container.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

font1=("Courier", 13)

entry = tk.Entry(container)
#entry.grid(row=5, column = 5, columnspan=1, rowspan=2)
entry.place(relx=0.4, rely=0.4)
play_button = tk.Button(container, text="Play!",font=font1, command=lambda: play_but_clicked())
play_button.place(relx=0.42, rely=0.45)

def play_but_clicked():
    global n_players
    n_players = int(entry.get())
    n_players = n_players
    time.sleep(0.2)
    entry.place_forget()
    play_button.place_forget()

    if n_players > 8:
        n_players = 8

    if n_players < 2:
        n_players = 2

    for num in range(int(n_players)):
        tok = "token" + str(num + 1)
        playing_tokens.append(tok)

    for num in range(int(n_players)):
        tok = "player" + str(num + 1)
        players.append(tok)
        player_names.update({tok:tok})

    global ask_info_frame
    ask_info_frame = tk.LabelFrame(container, text="Enter Your Details", bg="khaki", width=100, height=80)
    ask_info_frame.place(relx=0.4,rely=0.3)

    ask_obj1 = ask_info(0)
    ask_obj2 = ask_info(1)

    if "token3" in playing_tokens:
        ask_obj3 = ask_info(2)

    if "token4" in playing_tokens:
        ask_obj4 = ask_info(3)

    if "token5" in playing_tokens:
        ask_obj5 = ask_info(4)

    if "token6" in playing_tokens:
        ask_obj6 = ask_info(5)

    if "token7" in playing_tokens:
        ask_obj7 = ask_info(6)

    if "token8" in playing_tokens:
        ask_obj8 = ask_info(7)



class gui_monopoly():
    def __init__(self):
        global display_board_obj
        display_board_obj = monopoly_game()

        global token1, token2, token3, token4, token5, token6, token7, token8

        token1 = tk.Label(container, text="T1", width=2, height=1)
        token2 = tk.Label(container, text="T2", width=2, height=1)
        token3 = tk.Label(container, text="T3", width=2, height=1)
        token4 = tk.Label(container, text="T4", width=2, height=1)
        token5 = tk.Label(container, text="T5", width=2, height=1)
        token6 = tk.Label(container, text="T6", width=2, height=1)
        token7 = tk.Label(container, text="T7", width=2, height=1)
        token8 = tk.Label(container, text="T8", width=2, height=1)

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
            # print("token3 reporting sir!")
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

        token_objs = [t1, t2, t3, t4, t5, t6, t7, t8]

        for i in range(n_players):
            playing_token_id.append(token_objs[i])


class ask_info:
    def __init__(self, player_num):
        self.player_num = player_num
        self.player_str = players[player_num]
        #self.ask_colors()
        self.ask_player_names()
    def ask_player_names(self):
        self.pl = tk.Label(ask_info_frame, text="enter your nickname -" + players[self.player_num])
        self.pl.pack(side="top")
        self.pe = tk.Entry(ask_info_frame)
        self.pe.pack(side='top')
        self.pb = tk.Button(ask_info_frame, text="Enter", command=lambda: self.ok_but_clicked_name())
        self.pb.pack(side="top")
        
    def ok_but_clicked_name(self):
        if str(self.pe.get()) == '':
            self.pl.pack_forget()
            self.pe.pack_forget()
            self.pb.pack_forget()
            self.ask_colors()

        elif str(self.pe.get()) != '':
            player_names[self.player_str] = str(self.pe.get())
            self.pl.pack_forget()
            self.pe.pack_forget()
            self.pb.pack_forget()
            self.ask_colors()

    def ask_colors(self):
        self.l = tk.Label(ask_info_frame, text="enter your favourite color -" + player_names[self.player_str])
        self.l.pack(side='top')
        self.e = tk.Entry(ask_info_frame)
        self.e.pack(side="top")
        self.b = tk.Button(ask_info_frame, text="Ok", command=lambda: self.ok_but_clicked_color())
        self.b.pack(side="top")

    def ok_but_clicked_color(self):
        if str(self.e.get()) == '':
            self.l.pack_forget()
            self.e.pack_forget()
            self.b.pack_forget()

        elif str(self.e.get()) != '':
            if str(self.e.get()) in all_colors:
                colors[self.player_num] = str(self.e.get())
                self.l.pack_forget()
                self.e.pack_forget()
                self.b.pack_forget()
            else:
                self.l.pack_forget()
                self.e.pack_forget()
                self.b.pack_forget()

        if self.player_num+1 == n_players:
            ask_info_frame.place_forget()
            gui_monopoly()

"""
class ask_screen(tk.Frame):
    def __init__(self, parent):
        global entry, enter_button
        tk.Frame.__init__(self, parent)
        entry = tk.Entry(container)
        entry.pack()
        play_button = tk.Button(self, text="Play!", command=lambda: self.play_but_clicked())
        play_button.pack()
    def play_but_clicked(self):
        global n_players
        n_players = int(entry.get())
        self.n_players = n_players
        time.sleep(0.2)
        entry.pack_forget()
        if n_players > 8:
            n_players = 8
        if n_players < 2:
            n_players = 2
        for num in range(int(n_players)):
            tok = "token" + str(num + 1)
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
        token_objs = [t1, t2, t3, t4, t5, t6, t7, t8]
        for i in range(n_players):
            playing_token_id.append(token_objs[i])
        display_board_obj = monopoly_game()"""



"""
class ask_screen(tk.Frame):
    def __init__(self, parent):
        global entry, enter_button
        tk.Frame.__init__(self, parent)
        entry = tk.Entry(container)
        entry.pack()
        play_button = tk.Button(self, text="Play!", command=lambda: self.play_but_clicked())
        play_button.pack()

    def play_but_clicked(self):

        global n_players
        n_players = int(entry.get())
        self.n_players = n_players
        time.sleep(0.2)
        entry.pack_forget()

        if n_players > 8:
            n_players = 8

        if n_players < 2:
            n_players = 2

        for num in range(int(n_players)):
            tok = "token" + str(num + 1)
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

        token_objs = [t1, t2, t3, t4, t5, t6, t7, t8]

        for i in range(n_players):
            playing_token_id.append(token_objs[i])

        display_board_obj = monopoly_game()"""

class monopoly_game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        width = container.winfo_screenwidth()  # width of screen
        height = container.winfo_screenheight()  # height of screen
        width -= 325
        height -= 345
        width = width / 9
        height = height / 9
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

        free_parking = tk.Frame(container, width=160, height=140, bg="orange", highlightbackground="black",
                                highlightthickness=1)
        #free_parking_obj = property(free_parking, "free_parking", 0, 0)
        free_parking.grid(row=0, column=0)
        #kentucky_avenue = tk.Frame(container, width=width, height=140, bg="LightSteelBlue1",
        #                           highlightbackground="black",highlightthickness=1)
        global kentucky_avenue
        kentucky_avenue = property("kentucky_avenue",  0,1,width, 140, "light blue", 100 )

        #chance2 = tk.Frame(container, width=width, height=140, bg="LightSteelBlue1", highlightbackground="black",
        #                   highlightthickness=1)
        #chance2_obj = property(chance2, "chance2", 0, 2)
        #chance2.grid(row=0, column=2)
        global chance2
        chance2 = property("Chance", 0,2, width, 140, "orange", 0)

        indiana_avenue = tk.Frame(container, width=width, height=140, bg="LightSteelBlue1",
                                  highlightbackground="black",
                                  highlightthickness=1)
        #indiana_avenue_obj = property(indiana_avenue, "indiana_avenue", 0, 3)
        indiana_avenue.grid(row=0, column=3)
        illinois_avenue = tk.Frame(container, width=width, height=140, bg="LightSteelBlue1",
                                   highlightbackground="black",
                                   highlightthickness=1)
        #illinois_avenue_obj = property(illinois_avenue, "illinois_avenue", 0, 4)
        illinois_avenue.grid(row=0, column=4)
        b_and_o_railroad = tk.Frame(container, width=width, height=140, bg="LightSteelBlue1",
                                    highlightbackground="black",
                                    highlightthickness=1)
        b_and_o_railroad.grid(row=0, column=5)
        #b_and_o_railroad_obj = property(b_and_o_railroad, "b_and_o_railroad", 0, 5)

        atlantic_avenue = tk.Frame(container, width=width, height=140, bg="LightSteelBlue1",
                                   highlightbackground="black",
                                   highlightthickness=1)
        #atlantic_avenue_obj = property(atlantic_avenue, "atlantic_avenue", 0, 6)
        atlantic_avenue.grid(row=0, column=6)
        ventnor_avenue = tk.Frame(container, width=width, height=140, bg="LightSteelBlue1",
                                  highlightbackground="black",
                                  highlightthickness=1)
        #ventnor_avenue_obj = property(ventnor_avenue, "ventnor_avenue", 0, 7)
        ventnor_avenue.grid(row=0, column=7)

        water_works = tk.Frame(container, width=width, height=140, bg="LightSteelBlue1",
                               highlightbackground="black",
                               highlightthickness=1)
        #water_works_obj = property(water_works, "water_works", 0, 8)
        water_works.grid(row=0, column=8)

        marvin_garden = tk.Frame(container, width=width, height=140, bg="LightSteelBlue1",
                                 highlightbackground="black",
                                 highlightthickness=1)
        #marvin_garden_obj = property(marvin_garden, "marvin_garden", 0, 9)
        marvin_garden.grid(row=0, column=9)

        go_to_jail = tk.Frame(container, width=160, height=140, bg="yellow", highlightbackground="black",
                              highlightthickness=1)
        #go_to_jail_obj = property(go_to_jail, "go_to_jail", 0, 10)
        go_to_jail.grid(row=0, column=10)

        # left lane
        new_york_avenue = tk.Frame(container, width=160, height=height, bg="lightsteelblue",
                                   highlightbackground="black",
                                   highlightthickness=1)
        #global new_york_avenue_obj
        #new_york_avenue_obj = property(new_york_avenue, "pacific_avenue", 1, 0)
        new_york_avenue.grid(row=1, column=0)

        tennessee_avenue = tk.Frame(container, width=160, height=height, bg="lightsteelblue",
                                    highlightbackground="black",
                                    highlightthickness=1)
        #tennessee_avenue_obj = property(tennessee_avenue, "tennessee_avenue", 2, 0)
        tennessee_avenue.grid(row=2, column=0)

        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=3, column=0)
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=4, column=0)
        tk.Frame(container, width=160, height=height, bg='green', highlightbackground="black",
                 highlightthickness=1).grid(row=5, column=0)
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=6, column=0)
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=7, column=0)
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=8, column=0)
        tk.Frame(container, width=160, height=height, bg="yellow", highlightbackground="black",
                 highlightthickness=1).grid(row=9, column=0)

        # lower lane
        just = tk.Frame(container, width=160, height=140, bg="pink", highlightbackground="black",
                        highlightthickness=1).grid(row=10, column=0)
        place3 = tk.Frame(container, width=width, height=140, bg="pink", highlightbackground="black",
                          highlightthickness=1)
        place3.grid(row=10, column=1)
        tk.Frame(container, width=width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=2)
        tk.Frame(container, width=width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=3)
        tk.Frame(container, width=width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=4)
        tk.Frame(container, width=width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=5)
        tk.Frame(container, width=width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=6)
        tk.Frame(container, width=width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=7)
        tk.Frame(container, width=width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=8)
        tk.Frame(container, width=width, height=140, bg="pink", highlightbackground="black",
                 highlightthickness=1).grid(row=10, column=9)
        go_box = tk.Frame(container, width=160, height=140, bg="brown", highlightbackground="black",
                          highlightthickness=1)
        go_box.grid(row=10, column=10)

        # right lane
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=1, column=10)
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=2, column=10)
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=3, column=10)
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=4, column=10)
        tk.Frame(container, width=160, height=height, bg='green', highlightbackground="black",
                 highlightthickness=1).grid(row=5, column=10)
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=6, column=10)
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=7, column=10)
        tk.Frame(container, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
                 highlightthickness=1).grid(row=8, column=10)
        place = tk.Frame(container, width=160, height=height, bg="yellow", highlightbackground="black",
                         highlightthickness=1)
        place.grid(row=9, column=10)
        global status_frame
        status_frame = tk.LabelFrame(container, text="Status Box", bg="light green", fg="black",  highlightbackground="black",highlightthickness=1,width = 9*width+2, height=3*height )
        status_frame.place(relx=0.118, rely=0.2)
        global properties_dicto
        properties_dicto = {21:kentucky_avenue, 22:chance2}

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

        global dice
        dice = roll_dice()

class roll_dice(tk.Frame):

    def __init__(self):

        tk.Frame.__init__(self)

        global roll_dice_d
        roll_dice_d = tk.Button(container, text="Roll Dice!", bg="orange" ,font=font1, command=lambda: self.virtual_dice())
        roll_dice_d.grid(row=5, column=5)

    def virtual_dice(self):
        roll_dice_d.grid_forget()
        self.token_str = playing_tokens[chance]
        self.token_id = playing_token_id[chance]

        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        dice_roll = dice_roll1 + dice_roll2
        dice_roll = 22
        show_dice = tk.StringVar()
        label_dice = "Dice Roll = " + str(dice_roll)
        show_dice.set(label_dice)
        tk.Label(container, textvariable=show_dice, bg="green", fg="orange", width=12, height=2).grid(row=7,column=5)

        position = master_dictionary[self.token_str]["position"]

        position += dice_roll

        if position >= 40:
            position -= 40

        self.token_id.token_move(position)

        global end_turn
        end_turn = tk.Button(container, text="End Turn!",font=font1, command=lambda: self.end_turn_clicked())
        end_turn.grid(row=6, column=6)

    def end_turn_clicked(self):
        global chance

        position= master_dictionary[playing_tokens[chance]]["position"]
        properties_dicto[position].info_box.grid_forget()

        chance += 1
        max_chance = n_players

        if max_chance == chance:
            chance = 0

        end_turn.grid_forget()
        roll_dice_d.grid(row=5, column=5)

class Status_of_player:
    def __init__(self, chance, token_str):
        dummy_height= height*9
        dummy_width=width*3

        self.inferior_status_frame = tk.LabelFrame(status_frame, text = token_str)




class token:
    def __init__(self, token_id, token_str, player_str):
        self.token_id = token_id
        self.token_str = token_str
        self.player_str = player_str

    def my_special_init(self):

        self.dicto = {self.token_str: {"position": 0, "row": row_coordinates["go_box"], "column": column_coordinates["go_box"]}}
        self.dicto_2 = {self.player_str: {"token_id": self.token_id, "token_str": self.token_str, "money": 1500}}
        master_dictionary.update(self.dicto)
        master_dictionary.update(self.dicto_2)
        self.token_id.grid(row=10, column=10, sticky=sticky_id[self.token_str])

    def token_move(self, position):
        master_dictionary[self.token_str]["position"] = position
        p = place_num[position]
        row = row_coordinates[p]
        column = column_coordinates[p]
        self.token_id.grid_forget()
        self.token_id.grid(row=row, column=column, sticky=sticky_id[self.token_str])
        properties_dicto[position].show_details()

class property:
    def __init__(self,property_str, row, column, width, height, color, rent):
        self.property_str = property_str
        self.color= color
        self.prop_box = tk.Frame(container, width=width, height=height, bg=color)
        self.prop_box.grid(row=row, column=column)
        self.rent = rent

    def show_details(self):
        self.info_box = tk.Frame(container, relief="raised", highlightbackground="black",width = width*4, height=height*3,
                          highlightthickness=1)
        self.info_box.grid(rowspan = 4,columnspan=3,  row = 4, column = 1)

        """name_plate_dis = tk.LabelFrame(self.info_box, bg="green", text=self.property_str +"\n\n",  font=("Courier", 15), highlightbackground="black",
                          highlightthickness=1)
        name_plate_dis.pack(side="top")"""

        prop_name_dis = tk.Label(self.info_box, text="property:"+self.property_str +"\n", bg=self.color ,font=("Courier", 15), highlightbackground="black",
                          highlightthickness=1)
        prop_name_dis.pack(side="top")

        rent_dis = tk.Label(self.info_box, text="\trent: \t"+str(self.rent)+"\n", font=("Courier", 15), highlightbackground="black",
                          highlightthickness=1)
        rent_dis.pack(side="top")
        
        # pack one house price plus rent with houses

container.mainloop()

"""        # , buying_price, rent, house_price, one_house_rent, group)
        # , "rent":rent,buying price
        # "house_price":house_price, "one_house_rent":one_house_rent, "color_group":group}"""
