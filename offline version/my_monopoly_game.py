import tkinter as tk
import random
from game_coords import *
from initialising_everything import *
asf_x = 0
asf_y = 0
#------------------------------ ☺☺☻☻ PLEASE IGNORE ALL THE DOC-STRINGS! ☺☺☻☻-------------------------

container = tk.Tk()
width = container.winfo_screenwidth()  # width of screen
height = container.winfo_screenheight()  # height of screen

container.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))
start_frame= tk.Frame(container, width=width, height=height)
start_frame.grid(row=0, column=0, sticky="nsew")

font1=("Courier", 13)

entry = tk.Entry(start_frame)
#entry.grid(row=5, column = 5, columnspan=1, rowspan=2)
entry.place(relx=0.4, rely=0.4)
play_button = tk.Button(start_frame, text="Play!",font=font1, command=lambda: play_but_clicked())
play_button.place(relx=0.42, rely=0.44)

def show_colors():
    color_frame = tk.Frame(start_frame)
    color_frame.pack(side="left")
    number_of_rows = 35

    all_colors = ['AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'CadetBlue1', 'CadetBlue2','CadetBlue3', 'CadetBlue4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'DarkOrange1','DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3','DarkOrchid4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'DarkSlateGray1','DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'DeepPink2', 'DeepPink3', 'DeepPink4','DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'IndianRed1', 'IndianRed2', 'IndianRed3','IndianRed4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'LemonChiffon2', 'LemonChiffon3','LemonChiffon4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3','LightCyan4', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'LightSalmon2', 'LightSalmon3','LightSalmon4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'LightSteelBlue1','LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightYellow2', 'LightYellow3','LightYellow4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'MediumPurple1','MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'MistyRose2', 'MistyRose3', 'MistyRose4','NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4','OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4','PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3','RoyalBlue4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4','SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3','SlateGray4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'alice blue','antique white', 'aquamarine', 'aquamarine2', 'aquamarine4', 'azure', 'azure2', 'azure3', 'azure4','bisque', 'bisque2', 'bisque3', 'bisque4', 'blanched almond', 'blue', 'blue violet', 'blue2', 'blue4','brown1', 'brown2', 'brown3', 'brown4', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4','cadet blue', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate1', 'chocolate2', 'chocolate3','coral', 'coral1', 'coral2', 'coral3', 'coral4', 'cornflower blue', 'cornsilk2', 'cornsilk3','cornsilk4', 'cyan', 'cyan2', 'cyan3', 'cyan4', 'dark goldenrod', 'dark green', 'dark khaki','dark olive green', 'dark orange', 'dark orchid', 'dark salmon', 'dark sea green', 'dark slate blue','dark slate gray', 'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray','dodger blue', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floral white', 'forest green','gainsboro', 'ghost white', 'gold', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1','goldenrod2', 'goldenrod3', 'goldenrod4', 'gray', 'gray1', 'gray10', 'gray11', 'gray12', 'gray13','gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray2', 'gray20', 'gray21', 'gray22','gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray3', 'gray30', 'gray31','gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray4', 'gray40','gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray5', 'gray50','gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray6','gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69','gray7', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78','gray79', 'gray8', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87','gray88', 'gray89', 'gray9', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray97','gray98', 'gray99', 'green yellow', 'green2', 'green3', 'green4', 'honeydew2', 'honeydew3','honeydew4', 'hot pink', 'indian red', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2','khaki3', 'khaki4', 'lavender', 'lavender blush', 'lawn green', 'lemon chiffon', 'light blue','light coral', 'light cyan', 'light goldenrod', 'light goldenrod yellow', 'light grey', 'light pink','light salmon', 'light sea green', 'light sky blue', 'light slate blue', 'light slate gray','light steel blue', 'light yellow', 'lime green', 'linen', 'magenta2', 'magenta3', 'magenta4','maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'medium aquamarine', 'medium blue','medium orchid', 'medium purple', 'medium sea green', 'medium slate blue', 'medium spring green','medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'navajo white','navy', 'old lace', 'olive drab', 'orange', 'orange red', 'orange2', 'orange3', 'orange4', 'orchid1','orchid2', 'orchid3', 'orchid4', 'pale goldenrod', 'pale green', 'pale turquoise', 'pale violet red','papaya whip', 'peach puff', 'pink', 'pink1', 'pink2', 'pink3', 'pink4', 'plum1', 'plum2', 'plum3','plum4', 'powder blue', 'purple', 'purple1', 'purple2', 'purple3', 'purple4', 'red', 'red2', 'red3','red4', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'salmon1', 'salmon2', 'salmon3','salmon4', 'sandy brown', 'sea green', 'seashell2', 'seashell3', 'seashell4', 'sienna1', 'sienna2','sienna3', 'sienna4', 'sky blue', 'slate blue', 'slate gray', 'snow', 'snow2', 'snow3', 'snow4','spring green', 'steel blue', 'tan1', 'tan2', 'tan4', 'thistle', 'thistle1', 'thistle2', 'thistle3','thistle4', 'tomato', 'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2','turquoise3', 'turquoise4', 'violet red', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white smoke','yellow', 'yellow green', 'yellow2', 'yellow3', 'yellow4']
    row, col = 0, 0
    for color in all_colors:
        tk.Label(color_frame, text=color, background=color, font=(None, -10)).grid(row=row, column=col+1, sticky='nsew')
        row += 1
        if (row > number_of_rows):
            row = 0
            col += 1


def play_but_clicked():
    global n_players, color_but, playing_tokens, chances
    n_players = entry.get()

    if n_players in n_players:
        n_players = int(n_players)

        for num in range(int(n_players)):
            tok = "token" + str(num + 1)
            playing_tokens.append(tok)
            chances.update({tok:num})

        for num in range(int(n_players)):
            pal = "player" + str(num + 1)
            player_chances.append(pal)

        global ask_info_frame, color_frame, ask_color_frame
        color_frame = tk.LabelFrame(start_frame, text="Supported Colors", bg="medium spring green", width=100, height=80)
        ask_info_frame = tk.LabelFrame(start_frame, text="Enter Your Details", bg="khaki", width=100, height=80)
        ask_color_frame = tk.LabelFrame(start_frame, text="Enter your favourite colors", bg="khaki", width=100, height=80)
        ask_info_frame.pack(side="top")

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

class ask_info:
    def __init__(self, player_num):
        global player_chances
        self.player_num = player_num
        self.player_str = player_chances[player_num]
        self.token_str = playing_tokens[player_num]
        self.ask_player_names()

    def ask_player_names(self):
        self.pl = tk.Label(ask_info_frame, text="enter your nickname -" + player_chances[self.player_num])
        self.pl.pack(side="top",fill="x")
        self.pe = tk.Entry(ask_info_frame)
        self.pe.pack(side='top',fill="x")
        self.pb = tk.Button(ask_info_frame, text="Enter", command=lambda: self.ok_but_clicked_name())
        self.pb.pack(side="top",fill="x")
        
    def ok_but_clicked_name(self):
        global asf_x
        if str(self.pe.get()) == '':
            self.pl.pack_forget()
            self.pe.pack_forget()
            self.pb.pack_forget()
            asf_x +=1
            self.ask_colors()
        elif str(self.pe.get()) != '':
            player_names[self.player_str] = str(self.pe.get())
            self.pl.pack_forget()
            self.pe.pack_forget()
            self.pb.pack_forget()
            asf_x +=1
            self.ask_colors()
            
        if asf_x == n_players:
            ask_info_frame.pack_forget()
            show_colors()
            ask_color_frame.pack_configure(side="right")
            ask_color_frame.configure(bg="orange red")


    def ask_colors(self):
        self.l = tk.Label(ask_color_frame, text="enter your favourite color -" + player_names[self.player_str])
        self.l.pack(side='top',fill="x")
        self.e = tk.Entry(ask_color_frame)
        self.e.pack(side="top",fill="x")
        self.b = tk.Button(ask_color_frame, text="Ok", command=lambda: self.ok_but_clicked_color())
        self.b.pack(side="top" ,fill="x")

    def ok_but_clicked_color(self):
        global asf_y

        if str(self.e.get()) == '':
            self.l.pack_forget()
            self.e.pack_forget()
            self.b.pack_forget()
            asf_y +=1

        elif str(self.e.get()) != '':

            if str(self.e.get()) in all_colors:
                colors[self.token_str] = str(self.e.get())
                self.l.pack_forget()
                self.e.pack_forget()
                self.b.pack_forget()
                asf_y +=1

            else:
                self.l.pack_forget()
                self.e.pack_forget()
                self.b.pack_forget()
                asf_y +=1

        if asf_y == n_players:
            start_frame.grid_forget()
            gui_monopoly()

def gui_monopoly():
    global display_board_obj
    display_board_obj = monopoly_game()

    global token1, token2, token3, token4, token5, token6, token7, token8

    token1 = tk.Label(container, text="T1", width=2, height=1,bg=colors["token1"], highlightbackground="white",highlightthickness=1)
    token2 = tk.Label(container, text="T2", width=2, height=1,bg=colors["token2"], highlightbackground="white",highlightthickness=1)
    token3 = tk.Label(container, text="T3", width=2, height=1,bg=colors["token3"], highlightbackground="white",highlightthickness=1)
    token4 = tk.Label(container, text="T4", width=2, height=1,bg=colors["token4"], highlightbackground="white",highlightthickness=1)
    token5 = tk.Label(container, text="T5", width=2, height=1,bg=colors["token5"], highlightbackground="white",highlightthickness=1)
    token6 = tk.Label(container, text="T6", width=2, height=1,bg=colors["token6"], highlightbackground="white",highlightthickness=1)
    token7 = tk.Label(container, text="T7", width=2, height=1,bg=colors["token7"], highlightbackground="white",highlightthickness=1)
    token8 = tk.Label(container, text="T8", width=2, height=1,bg=colors["token8"], highlightbackground="white",highlightthickness=1)

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

    stat1 = Status_of_player("token1",player_names["player1"])
    stat2 = Status_of_player("token2",player_names["player2"])
    stat3 = Status_of_player("token3",player_names["player3"])
    stat4 = Status_of_player("token4",player_names["player4"])
    stat5 = Status_of_player("token5",player_names["player5"])
    stat6 = Status_of_player("token6",player_names["player6"])
    stat7 = Status_of_player("token7",player_names["player7"])
    stat8 = Status_of_player("token8",player_names["player8"])

    stat1.display()
    stat1.raise_relief()
    stat2.display()

    if "token3" in playing_tokens:
        t3.my_special_init()
        stat3.display()
    if "token4" in playing_tokens:
        t4.my_special_init()
        stat4.display()
    if "token5" in playing_tokens:
        t5.my_special_init()
        stat5.display()
    if "token6" in playing_tokens:
        t6.my_special_init()
        stat6.display()
    if "token7" in playing_tokens:
        t7.my_special_init()
        stat7.display()
    if "token8" in playing_tokens:
        t8.my_special_init()
        stat8.display()

    global stat_objs
    stat_objs = [stat1, stat2,stat3, stat4,stat5, stat6,stat7, stat8]
    token_objs = [t1, t2, t3, t4, t5, t6, t7, t8]

    for i in range(n_players):
        playing_token_obj_id.append(token_objs[i])

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


        free_parking = tk.Frame(container, width=160, height=140, bg="orange", highlightbackground="black",highlightthickness=1)
        free_parking.grid(row=0, column=0)

        kentucky_avenue = property("kentucky_avenue",  0,1,width, 140, "light blue", 100 , 200, 50, 60,70,80,100,100,50,40,"bottom")

        #chance2 = tk.Frame(container, width=width, height=140, bg="LightSteelBlue1", highlightbackground="black",
        #                   highlightthickness=1)
        #chance2_obj = property(chance2, "chance2", 0, 2)
        #chance2.grid(row=0, column=2)
        global chance2
        chance2 = property("Chance", 0,2, width, 140, "orange", 0, 0, 100 , 200, 50, 60,70,80,100,70 )

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
                                   highlightbackground="black",highlightthickness=1)
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

        monopoly_dis = tk.Label(container, text="Monopoly", bg="tomato1", fg="white", font=font1)
        monopoly_dis.grid(row=5, column=5)

        global status_frame,sf_width,sf_height
        sf_width = 8*width+2
        sf_height = 3*height
        status_frame = tk.LabelFrame(container, text="Status Box", bg="light green", fg="black",  highlightbackground="black",highlightthickness=1,width = sf_width, height=sf_height )
        status_frame.grid(rowspan=4,columnspan=9,row=1,column=1)
        global properties_dicto
        properties_dicto = {21:kentucky_avenue, 22:chance2}

        global dice
        dice = roll_dice()

class roll_dice(tk.Frame):

    def __init__(self):

        tk.Frame.__init__(self)

        global roll_dice_d
        roll_dice_d = tk.Button(container, text="Roll Dice!", bg="orange" ,font=font1, command=lambda: self.virtual_dice())
        roll_dice_d.grid(row=6, column=6)

    def virtual_dice(self):
        roll_dice_d.grid_forget()
        self.token_str = playing_tokens[chance]
        self.token_id = playing_token_obj_id[chance]

        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        dice_roll = dice_roll1 + dice_roll2
        dice_roll = 21
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
        properties_dicto[position].info_box1.grid_forget()
        properties_dicto[position].info_box2.grid_forget()
        properties_dicto[position].buy_button.grid_forget()
        stat_objs[chance].normal_relief()

        chance += 1
        max_chance = n_players

        stat_objs[chance].raise_relief()

        if max_chance == chance:
            chance = 0

        end_turn.grid_forget()
        roll_dice_d.grid(row=5, column=5)

class Status_of_player:
    def __init__(self, token_str, player_str):
        self.token_str = token_str
        self.player_str = player_str
    def display(self):
        self.inferior_status_frame = tk.LabelFrame(status_frame, text=self.player_str, bg=colors[self.token_str], relief="flat",
                                                   width=sf_width / n_players, height=sf_height, font=("white",11), bd=7)

        if chance == chances[self.token_str]:
            self.inferior_status_frame["relief"] = "raised"

        self.inferior_status_frame.pack(side="left")

    def raise_relief(self):
        self.inferior_status_frame["relief"] = "raised"

    def normal_relief(self):
        self.inferior_status_frame["relief"] = "flat"

class token:
    def __init__(self, token_id, token_str, player_str):
        self.token_id = token_id
        self.token_str = token_str
        self.player_str = player_str

    def my_special_init(self):

        self.dicto = {self.token_str: {"position": 0, "row": row_coordinates["go_box"], "column": column_coordinates["go_box"]}}
        self.dicto_2 = {self.player_str: {"token_id": self.token_id, "token_str": self.token_str, "money": 1800}}
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
        properties_dicto[position].property_manager()

class property:
    def __init__(self,property_str, row, column, width, height, color, rent, price, one_house_rent, two_house_rent,
                 three_house_rent,four_house_rent,hotel_rent,cost_of_house,cost_of_hotel, mortgage_value, color_box_side=None):
        self.property_str = property_str
        self.width = width
        self.height = height
        self.one_house_rent = one_house_rent
        self.two_house_rent  = two_house_rent
        self.three_house_rent = three_house_rent
        self.four_house_rent = four_house_rent
        self.hotel_rent = hotel_rent
        self.cost_of_hotel = cost_of_hotel
        self.mortgage_value = mortgage_value
        self.price = price
        self.color= color
        self.rent = rent
        self.cost_of_house = cost_of_house

        prop_info.update({self.property_str:{"price":self.price, "houses":0, "owner":None, "players on site":[]}})


        if self.property_str not in special_properties:
            self.prop_box = tk.Frame(container, width=width, height=height,highlightbackground="black" ,highlightthickness=1)
            self.prop_box.grid(row=row, column=column)
            self.color_box = tk.Frame(container, bg=self.color,highlightbackground="black" ,highlightthickness=1 , width=self.width, height=self.height/4)
            self.color_box.grid(row=row, column=column, sticky = "s")
            self.buy_button = tk.Button(container, text="Buy", bg=self.color,font=font1 , command=lambda :self.buy_prop())

        if self.property_str in special_properties:
            pass

    def property_manager(self):
        self.show_details()
        prop_info[self.property_str]["players on site"] = player_names[player_chances[chance]]

        if prop_info[self.property_str]["owner"] == None:
            self.buy_button.grid(row=6, column=8)

        if prop_info[self.property_str]["owner"] != None:
            if prop_info[self.property_str]["owner"] ==  prop_info[self.property_str]["players on site"][-1]:
                print("non owner on site")
                print(prop_info)
                # dev here (TRADE option or build house)
            if prop_info[self.property_str]["owner"] ==  prop_info[self.property_str]["players on site"][-1]:
                print("owner on site")
                print(prop_info)
                # dev here (take rent)

    def buy_prop(self):
        print("buying property!")
        self.buy_button.grid_forget()
        prop_info[self.property_str]["owner"] = player_chances[chance]
        tk.Label(container, text=player_chances[chance]+" successfully bought-"+self.property_str,bg=self.color).grid(columnspan=3,row=6,column=6)
        print(prop_info)

    def show_details(self):

        self.info_box1 = tk.Frame(container, relief="raised", highlightbackground="black",width = width*4, height=height*4,
                          highlightthickness=1)
        self.info_box1.grid(rowspan = 6,columnspan=2,  row = 4, column = 1)

        self.info_box2 = tk.Frame(container, relief="raised", highlightbackground="black",width = width*4, height=height*4,
                          highlightthickness=1)
        self.info_box2.grid(rowspan = 6,columnspan=2,  row = 4, column = 3)


        self.prop_name_dis = tk.Label(self.info_box1, text=self.property_str, bg=self.color ,font=("Courier", 12), highlightbackground="black",
                          highlightthickness=1)
        self.prop_name_dis.pack(side="top" , fill="x")

        self.rent_dis = tk.Label(self.info_box1, text="RENT- SITE ONLY: "+str(self.rent), font=("Courier", 12), highlightbackground="black",
                          highlightthickness=1)
        self.rent_dis.pack(side="top" )

        self.house1 = tk.Label(self.info_box1, text="RENT- with 1 house: "+str(self.one_house_rent), font=("Courier", 12), highlightbackground="black",
                          highlightthickness=1)
        self.house1.pack(side="top" )
        self.house2 = tk.Label(self.info_box1, text="RENT-with 2 houses: "+str(self.two_house_rent), font=("Courier", 12), highlightbackground="black",
                          highlightthickness=1)
        self.house2.pack(side="top" )

        self.house3 = tk.Label(self.info_box1, text="RENT-with 3 houses: "+str(self.three_house_rent), font=("Courier", 12), highlightbackground="black",
                          highlightthickness=1)
        self.house3.pack(side="top" )
        self.house4 = tk.Label(self.info_box1, text="RENT-with 4 houses: "+str(self.four_house_rent), font=("Courier", 12), highlightbackground="black",
                          highlightthickness=1)
        self.house4.pack(side="top" )

        self.hotel = tk.Label(self.info_box2, text="RENT- with HOTEL: " + str(self.hotel_rent) ,
                               font=("Courier", 12), highlightbackground="black",
                               highlightthickness=1)
        self.hotel.pack(side="top" )

        self.cost_of_house_dis = tk.Label(self.info_box2, text="cost of one house: " + str(self.cost_of_house) ,
                               font=("Courier", 12), highlightbackground="black",
                               highlightthickness=1)
        self.cost_of_house_dis.pack(side="top" )


        self.cost_hotel = tk.Label(self.info_box2, text="cost of hotel: " + str(self.cost_of_hotel)+"\n+four houses",
                               font=("Courier", 12), highlightbackground="black",
                               highlightthickness=1)
        self.cost_hotel.pack(side="top" )


        self.mortgage_value_dis = tk.Label(self.info_box2, text="Mortgage value: " + str(self.mortgage_value) ,
                               font=("Courier", 12), highlightbackground="black",
                               highlightthickness=1)
        self.mortgage_value_dis.pack(side="top" )



container.mainloop()
