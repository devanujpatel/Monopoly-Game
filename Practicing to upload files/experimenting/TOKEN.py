# make all initializing in the initialising file ---> lately it would become easy to make a save feature

# making a class of token and then will coordinate with roll dice
# everything is associated with roll dice!

from tkinter import *
import time,random,tkinter
from grid_and_place_coordinates import *
from initialising_everything import *

#keyboard.add_hotkey('shift+d', lambda:destroy_root())
root = Tk()
width = root.winfo_screenwidth()  # width of screen
height = root.winfo_screenheight()  # height of screen

class Window(Frame):
    def __int__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.width = width
        self.height = height
        self.monopoly()
        self.monopoly()

        self.token1 = tkinter.Label(self, text="T1", bg="light green", width=2, height=1)
        self.token2 = tkinter.Label(self, text="T2", bg="light green", width=2, height=1)
        self.token3 = tkinter.Label(self, text="T3", bg="light green", width=2, height=1)
        self.token4 = tkinter.Label(self, text="T4", bg="light green", width=2, height=1)
        self.token5 = tkinter.Label(self, text="T5", bg="light green", width=2, height=1)
        self.token6 = tkinter.Label(self, text="T6", bg="light green", width=2, height=1)
        self.token7 = tkinter.Label(self, text="T7", bg="light green", width=2, height=1)
        self.token8 = tkinter.Label(self, text="T8", bg="light green", width=2, height=1)

    def monopoly(self):

        self.master.title("☺Monopoly☺")

        # allowing the widget to take the full space of the self window
        self.pack(fill=BOTH, expand=1)
        self.width-=320
        self.height-=340
        self.width=self.width / 9
        self.height = self.height / 9
    
        #upper lane
        # start naming ☻
        free_parking = tkinter.Frame(self,width=160,height=140,bg="orange",  highlightbackground="black",
                             highlightthickness=1).grid(row=0,column=0)
        tkinter.Frame(self,  width=self.width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                             highlightthickness=1).grid(row=0, column=1)
        tkinter.Frame(self,  width=self.width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                             highlightthickness=1).grid(row=0, column=2)
        tkinter.Frame(self,  width=self.width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                             highlightthickness=1).grid(row=0, column=3)
        tkinter.Frame(self,  width=self.width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                             highlightthickness=1).grid(row=0, column=4)
        tkinter.Frame(self,  width=self.width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                             highlightthickness=1).grid(row=0, column=5)
        tkinter.Frame(self,  width=self.width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                             highlightthickness=1).grid(row=0, column=6)
        tkinter.Frame(self,  width=self.width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                             highlightthickness=1).grid(row=0, column=7)
        tkinter.Frame(self,  width=self.width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                             highlightthickness=1).grid(row=0, column=8)
        tkinter.Frame(self,  width=self.width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                             highlightthickness=1).grid(row=0, column=9)
        go_jail = tkinter.Frame(self,width=160,height=140,bg="yellow",  highlightbackground="black",
                             highlightthickness=1).grid(row=0,column=10)
    
        #left lane
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=1, column=0)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=2, column=0)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=3, column=0)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=4, column=0)
        tkinter.Frame(self, width=160, height = self.height, bg='green',  highlightbackground="black",
                             highlightthickness=1).grid(row=5, column=0)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=6, column=0)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=7, column=0)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=8, column=0)
        tkinter.Frame(self, width=160, height = self.height, bg="yellow",  highlightbackground="black",
                             highlightthickness=1).grid(row=9, column=0)
    
        #lower lane
        just = tkinter.Frame(self, width=160, height=140, bg="pink",  highlightbackground="black",
                             highlightthickness=1).grid(row=10, column=0)
        tkinter.Frame(self, width=self.width, height=140,  bg="pink", highlightbackground="black",
                      highlightthickness=1).grid(row=10, column=1)
        tkinter.Frame(self, width=self.width, height=140,  bg="pink", highlightbackground="black",
                      highlightthickness=1).grid(row=10, column=2)
        tkinter.Frame(self, width=self.width, height=140,  bg="pink", highlightbackground="black",
                      highlightthickness=1).grid(row=10, column=3)
        tkinter.Frame(self, width=self.width, height=140,  bg="pink", highlightbackground="black",
                      highlightthickness=1).grid(row=10, column=4)
        tkinter.Frame(self, width=self.width, height=140,  bg="pink", highlightbackground="black",
                      highlightthickness=1).grid(row=10, column=5)
        tkinter.Frame(self, width=self.width, height=140,  bg="pink", highlightbackground="black",
                      highlightthickness=1).grid(row=10, column=6)
        tkinter.Frame(self, width=self.width, height=140,  bg="pink", highlightbackground="black",
                      highlightthickness=1).grid(row=10, column=7)
        tkinter.Frame(self, width=self.width, height=140,  bg="pink", highlightbackground="black",
                      highlightthickness=1).grid(row=10, column=8)
        tkinter.Frame(self, width=self.width, height=140,  bg="pink", highlightbackground="black",
                      highlightthickness=1).grid(row=10, column=9)
        go_box = tkinter.Frame(self, width=160, height=140,  bg="brown", highlightbackground="black",
                               highlightthickness=1)
        go_box.grid(row=10, column=10)
    
        # right lane
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=1, column=10)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=2, column=10)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=3, column=10)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=4, column=10)
        tkinter.Frame(self, width=160, height = self.height, bg='green',  highlightbackground="black",
                             highlightthickness=1).grid(row=5, column=10)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=6, column=10)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=7, column=10)
        tkinter.Frame(self, width=160, height = self.height, bg="lightsteelblue",  highlightbackground="black",
                             highlightthickness=1).grid(row=8, column=10)
        tkinter.Frame(self, width=160, height = self.height, bg="yellow",highlightbackground="black",
                            highlightthickness=1).grid(row=9, column=10)
    
    #show_board()
    
    def show(self,widget,row,column):
        widget.grid(row=row,column=column)

    def no_name(self):
        entry_wid = tkinter.Entry(self, text="Enter number of players")
        play_button = tkinter.Button(self, text="PLAY!", command=self.play_button_clicked())
        self.entry_wid = entry_wid
        self.play_button = play_button
        self.show(entry_wid, 3, 5)
        self.show(play_button, 4, 5)

    def play_button_clicked(self):
        global n_players
        self.entry = self.entry_wid.get()
        n_players = int(self.entry)
    
        """favourable_n_players = []
        for p in range(8):
            tok = "token"+str(p+1)
            favourable_n_players.append(tok)"""
    
        if n_players>8:
            n_players=8
    
        if n_players<2:
            n_players=2
    
        time.sleep(0.2)
        self.entry_wid.grid_forget()
        self.play_button.grid_forget()
        # display enjoy
        self.initialise(n_players)
    
    def initialise(self,n_players):
        global chance,playing_tokens
    
        chance = 0
    
        for num in range(int(n_players)):
            tok = "token" + str(num+1)
            playing_tokens.append(tok)
    
        t1 = Token(self.token1,"token1","player1","blue",0,1)
        t2 = Token(self.token2,"token2","player2","blue",0,1)
    
        if "token3" in playing_tokens:
            t3 = Token(self.token3, "token3", "player3", "blue", 0, 1)
    
        if "token4" in playing_tokens:
            t4 = Token(self.token4, "token4", "player4", "blue", 0, 1)
    
        if "token5" in playing_tokens:
            t5 = Token(self.token5, "token5", "player5", "blue", 0, 1)
    
        if "token5" in playing_tokens:
            t6 = Token(self.token6, "token6", "player6", "blue", 0, 1)
    
        if "token5" in playing_tokens:
            t7 = Token(self.token7, "token7", "player7", "blue", 0, 1)
    
        if "token8" in playing_tokens:
            t8 = Token(self.token8, "token8", "player8", "blue", 0, 1)



    """
    #token1 = tkinter.Label(self,text="T1",self.width=2,height=1)
    token1.grid(row=10,column=10)
    #token2 = tkinter.Label(self,text="T2",self.width=2,height=1)
    token2.grid(row=10,column=10)
    master_dictionary["tokens"]["token1"] = {"position":0, "row":row_coordinates['go_box'], "column":column_coordinates['go_box']}
    master_dictionary["tokens"]["token2"] = {"position":0, "row":row_coordinates['go_box'], "column":column_coordinates['go_box']}

    master_dictionary["players"]["player1"] = {"token":"token1","money":1500}
    master_dictionary["players"]["player2"] = {"token": "token2", "money": 1500}


    if "token3" in playing_tokens:
        #token3 = tkinter.Label(self,text="T3",self.width=2,height=1)
        token3.grid(row=10, column=10)
        master_dictionary["tokens"]["token3"] = {"position": 0, "row": row_coordinates['go_box'],"column": column_coordinates['go_box']}
        master_dictionary["players"]["player3"] = {"token": "token3", "money": 1500}

    if "token4" in playing_tokens:
        #token4 = tkinter.Label(self,text="T4",self.width=2,height=1)
        token4.grid(row=10, column=10)
        master_dictionary["tokens"]["token4"] = {"position": 0, "row": row_coordinates['go_box'],"column": column_coordinates['go_box']}
        master_dictionary["players"]["player4"] = {"token": "token4", "money": 1500}

    if "token5" in playing_tokens:
        #token5 = tkinter.Label(self,text="T5",self.width=2,height=1)
        token5.grid(row=10, column=10)
        master_dictionary["tokens"]["token5"] = {"position": 0, "row": row_coordinates['go_box'],"column": column_coordinates['go_box']}
        master_dictionary["players"]["player5"] = {"token": "token5", "money": 1500}

    if "token6" in playing_tokens:
        #token6 = tkinter.Label(self,text="T6",self.width=2,height=1)
        token6.grid(row=10, column=10)
        master_dictionary["tokens"]["token6"] = {"position": 0, "row": row_coordinates['go_box'],"column": column_coordinates['go_box']}
        master_dictionary["players"]["player6"] = {"token": "token6", "money": 1500}

    if "token7" in playing_tokens:
        #token7 = tkinter.Label(self,text="T7",self.width=2,height=1)
        token7.grid(row=10, column=10)
        master_dictionary["tokens"]["token7"] = {"position": 0, "row": row_coordinates['go_box'],"column": column_coordinates['go_box']}
        master_dictionary["players"]["player7"] = {"token": "token7", "money": 1500}

    if "token8" in playing_tokens:
        #token8 = tkinter.Label(self,text="T8",self.width=2,height=1)
        token8.grid(row=10, column=10)
        master_dictionary["tokens"]["token8"] = {"position": 0, "row": row_coordinates['go_box'],"column": column_coordinates['go_box']}
        master_dictionary["players"]["player8"] = {"token": "token8", "money": 1500}"""

    # working properly-
    #print(playing_tokens)
    #print(master_dictionary)

    """roll_dice_obj = Roll_dice(0,"sky blue","token1")
    roll_dice_obj.show_dice_button()"""

"""token2 = tkinter.Label(self,text="T2",self.width=2,height=1)
master_dictionary["players"]["player2"] = {"token": token2, "money": 1500}
master_dictionary["players"]["player2"]["token"].grid(row=10,column=10)
"""

"""
token1 = tkinter.Label(go_box, text="T1", self.width=2, height=1)
token1.place(relx=0.5, rely=0.5)
token2 = tkinter.Label(go_box, text="T2", self.width=2, height=1)
token2.place(relx=0.1, rely=0.5)"""

class Roll_dice:
    def __init__(self,chance,color,token):
        self.chance = int(chance)
        self.token = token
        self.color = color
        self.rolling_dice(token)

    def rolling_dice(self,token):
        dice_roll = random.randint(1, 6)
        position = master_dictionary["tokens"][token]["position"]
        position += dice_roll

        show_dice = tkinter.StringVar()
        label_dice = "Dice Roll = " + str(dice_roll)
        show_dice.set(label_dice)
        # change place here
        # tkinter.Label(root, textvariable=show_dice, bg="green", fg="orange", width=12, height=3).place(relx=0.5,rely=0.5,x=80, y=8)

        if position >= 40:
            position -= 40
    def show_dice_button(self):
        roll_dice_but = tkinter.Button(root,text="Roll Dice",fg="black",bg=self.color,command=lambda:rolling_dice(self.token),width=18, height=3)
        #show(roll_dice_but,4,6)

    def monopoly_manager(self):
        pass

class Token():
    def __init__(token,token_id,token_str,player_str,color,dice_roll_num,position_on_board):
        """
        token.color = color
        token.dice_roll_num = dice_roll_num"""
        token.position_on_board = position_on_board
        token.row = row_coordinates[place_num[position_on_board]]
        token.column = column_coordinates[place_num[position_on_board]]
        token.token_id = token_id
        token.token_str = token_str
        token.player_str  = player_str
        print(token_id)
        master_dictionary["tokens"][token_str] = {"position": 0, "row": row_coordinates['go_box'],"column": column_coordinates['go_box']}
        master_dictionary["players"][player_str] = {"token": token_str, "money": 1500}
        token_id.grid(row=10, column=10)


        def init_tokens():

            #master_dictionary["tokens"]["token_id"].grid(row=master_dictionary["tokens"][token_str]["row"],column=master_dictionary["tokens"][token_str]["column"])
            print(master_dictionary)
        
    def move_tokens(token):
        pass
#token_obj = Token(token1,'token',"player1","blue",0,6)




root.geometry("%dx%d%+d%+d" % (width, height, 0, 0))
game = Window(root)

root.mainloop()

