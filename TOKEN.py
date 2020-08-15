# make all initializing in the initialising file ---> lately it would become easy to make a save feature

# making a class of token and then will coordinate with roll dice
# everything is associated with roll dice! 

import tkinter
from initialising_everything import *

import time
root = tkinter.Tk()

width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight() # height of screen

root.geometry("%dx%d%+d%+d" % (width, height, 0 ,0))

token1 = tkinter.Label(root, text="T1", bg="light green", width=2, height=1)
token2 = tkinter.Label(root, text="T2", bg="light green", width=2, height=1)
token3 = tkinter.Label(root, text="T3", bg="light green", width=2, height=1)
token4 = tkinter.Label(root, text="T4", bg="light green", width=2, height=1)
token5 = tkinter.Label(root, text="T5", bg="light green", width=2, height=1)
token6 = tkinter.Label(root, text="T6", bg="light green", width=2, height=1)
token7 = tkinter.Label(root, text="T7", bg="light green", width=2, height=1)
token8 = tkinter.Label(root, text="T8", bg="light green", width=2, height=1)

width-=320
height-=340
width = width / 9
height = height / 9

#upper lane
free_parking = tkinter.Frame(root,width=160,height=140,bg="orange",  highlightbackground="black",
                     highlightthickness=1).grid(row=0,column=0)
tkinter.Frame(root,  width = width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                     highlightthickness=1).grid(row=0, column=1)
tkinter.Frame(root,  width = width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                     highlightthickness=1).grid(row=0, column=2)
tkinter.Frame(root,  width = width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                     highlightthickness=1).grid(row=0, column=3)
tkinter.Frame(root,  width = width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                     highlightthickness=1).grid(row=0, column=4)
tkinter.Frame(root,  width = width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                     highlightthickness=1).grid(row=0, column=5)
tkinter.Frame(root,  width = width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                     highlightthickness=1).grid(row=0, column=6)
tkinter.Frame(root,  width = width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                     highlightthickness=1).grid(row=0, column=7)
tkinter.Frame(root,  width = width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                     highlightthickness=1).grid(row=0, column=8)
tkinter.Frame(root,  width = width, height=140,bg = "LightSteelBlue1",  highlightbackground="black",
                     highlightthickness=1).grid(row=0, column=9)
go_jail = tkinter.Frame(root,width=160,height=140,bg="yellow",  highlightbackground="black",
                     highlightthickness=1).grid(row=0,column=10)

#left lane
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=1, column=0)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=2, column=0)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=3, column=0)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=4, column=0)
tkinter.Frame(root, width=160, height=height, bg='green',  highlightbackground="black",
                     highlightthickness=1).grid(row=5, column=0)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=6, column=0)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=7, column=0)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=8, column=0)
tkinter.Frame(root, width=160, height=height, bg="yellow",  highlightbackground="black",
                     highlightthickness=1).grid(row=9, column=0)

#lower lane
just = tkinter.Frame(root, width=160, height=140, bg="pink",  highlightbackground="black",
                     highlightthickness=1).grid(row=11, column=0)
tkinter.Frame(root, width=width, height=140,  bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=1)
tkinter.Frame(root, width=width, height=140,  bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=2)
tkinter.Frame(root, width=width, height=140,  bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=3)
tkinter.Frame(root, width=width, height=140,  bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=4)
tkinter.Frame(root, width=width, height=140,  bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=5)
tkinter.Frame(root, width=width, height=140,  bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=6)
tkinter.Frame(root, width=width, height=140,  bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=7)
tkinter.Frame(root, width=width, height=140,  bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=8)
tkinter.Frame(root, width=width, height=140,  bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=9)
go_box = tkinter.Frame(root, width=160, height=140,  bg="brown", highlightbackground="black",
                       highlightthickness=1).grid(row=11, column=10)

# right lane
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=1, column=10)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=2, column=10)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=3, column=10)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=4, column=10)
tkinter.Frame(root, width=160, height=height, bg='green',  highlightbackground="black",
                     highlightthickness=1).grid(row=5, column=10)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=6, column=10)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=7, column=10)
tkinter.Frame(root, width=160, height=height, bg="lightsteelblue",  highlightbackground="black",
                     highlightthickness=1).grid(row=8, column=10)
tkinter.Frame(root, width=160, height=height, bg="yellow",highlightbackground="black",
                    highlightthickness=1).grid(row=9, column=10)






entry = tkinter.Entry(root,text="Enter number of players",width=40,height=5)
play_button = tkinter.Button(root,text="PLAY!")

def show(widget,row,column):
    widget.grid(row=row,column=column)

show(entry,3,6)
show(play_button,4,6)

class Roll_dice:
    def __init(self,chance):
        self.chance = chance
    pass

class Token:
    def __init__(token,token_name,color,dice_roll_num,position_on_board,one_time_init):
        token.token_name = token_name
        token.color = color
        token.dice_roll_num = dice_roll_num
        token.position_on_board = position_on_board
        token.one_time_init = one_time_init
        token.n_players = entry.get()
        
    def one_time_init_tokens(token):

        if token.one_time_init:
            for num in token.n_players:
                tok = "token"+num
                playing_tokens.append(tok)

        if "token1" in playing_tokens:
            pass



            
            
            


root.mainloop()
        