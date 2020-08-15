from flexible_board import *
from coordinates_of_our_places import *
import random

entry = tkinter.Entry(root)
def show_entry():
    entry.grid(row=2, column=5)

show_entry()

def initializing():
    global n_players, show_button, turn_num

    n_players = int(entry.get())

    num = 1

    for n in range(n_players):
        token_name = "token" + str(num)
        tokens.update({token_name: ""})

        player_name = "player" + str(num)
        player_props.update({player_name: ""})

        player_prop_num.update({player_name: 0})

        num += 1

    working_lists()

def play_button_clicked():
    global n_players, entry, forget, go_ahead

    n_players = entry.get()
    n_players = int(n_players)
    time.sleep(0.4)

    entry.grid_forget()
    play_button.grid_forget()
    # show_enjoy()

    initializing()
    display_tokens(n_players)

play_button = tkinter.Button(text='PLAY!', command=play_button_clicked)
def show_button():
    play_button.grid(row=3, column=5)

show_button()

# make changes here when making save option!
player_props = {}
tokens = {}
player_prop_num = {}
playing_tokens = []

def working_lists():
    num = 1
    for i in range(n_players):
        tok = "token" + str(num)
        playing_tokens.append(tok)
        num += 1


monopoly_display = tkinter.Label(root, text="MONOPOLY", bg="brown", fg="white", font=("Times New Roman", 18, "bold"))
monopoly_display.place(relx=0.5, rely=0.5, anchor="center")

roll_dice_button = tkinter.Button(root, text="Roll Dice", bg="orange", fg="black", command=lambda: roll_dice(),
                                  width=18, height=3)

roll_dice_button.place(relx=0.5, rely=0.5, x=-68, y=60)
#roll_dice_button.grid(row=7, column=5)

position = 0

# place(relx=0.5, rely=0.5,x=80, y=8)

def initialize_all_tokens():
    global token1,token2,token3,token4,token5,token6,token7,token8
    token1 = tkinter.Label(root,text="T1",bg="light green",width=2,height=1)
    token2 = tkinter.Label(root,text="T2",bg="light green",width=2,height=1)
    token3 = tkinter.Label(root,text="T",bg="light green",width=2,height=1)
    token4 = tkinter.Label(root,text="T",bg="light green",width=2,height=1)
    token5 = tkinter.Label(root,text="T",bg="light green",width=2,height=1)
    token6 = tkinter.Label(root,text="T",bg="light green" ,width=2,height=1)
    token7 = tkinter.Label(root,text="T",bg="light green",width=2,height=1)
    token8 = tkinter.Label(root,text="T",bg="light green",width=2,height=1)

# MAKE CHANGES HERE WHILE MAKING SAVE FEATURE
initialize_all_tokens()

def display_tokens(n_players):

    global last_turn,chance

    chance = 1

    if n_players == 0 or n_players == 1 or n_players == 2:
        token1.grid(row=row_coordinates["go_box"],column=column_coordinates["go_box"])
        token2.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        last_turn = 2

    if n_players == 3:
        token1.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        token2.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        token3.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        last_turn = 3

    if n_players == 4:
        token1.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        token2.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        token3.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        token4.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        last_turn = 4


    if n_players == 5:
        token1.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        token2.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        token3.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        token3.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        token4.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        token5.grid(row=row_coordinates["go_box"], column=column_coordinates["go_box"])
        last_turn = 5

def roll_dice():

    global position, dice_val
    dice_val = random.randint(1, 6)
    position += dice_val
    show_dice = tkinter.StringVar()
    label_dice = "Dice Roll = " + str(dice_val)
    show_dice.set(label_dice)
    tkinter.Label(root, textvariable=show_dice, bg="green", fg="orange", width=12, height=3). place(relx=0.5, rely=0.5,x=80, y=8)
    if position >= 40:
        position = position - 40

    move_token()

def forget_widget(widget):
    widget.grid_forget()

def move_token():
    global position, chance,last_turn
    print(chance,last_turn)
    for place in myplaces:

        if position == myplace_num[place]:

            if chance == 1:
                forget_widget(token1)
                token1.grid(row=row_coordinates[place], column=column_coordinates[place])
                tokens["token1"] = place
                chance += 1
                if chance == last_turn:
                    chance = 1

            if chance == 2:
                forget_widget(token2)
                token1.grid(row=row_coordinates[place], column=column_coordinates[place])
                tokens["token2"] = place
                chance += 1
                if chance == last_turn:
                    chance = 1

            if chance == 3:

                forget_widget(token3)
                token1.grid(row=row_coordinates[place], column=column_coordinates[place])
                tokens["token3"] = place
                chance += 1
                if chance == last_turn:
                    chance = 1

            # this should never run!(until and unless there is a ptoblem in our code above^^^)
            if chance == last_turn:
                chance = 1
                print("problem in handling chance!!")

            """ forget_widget()
                token1 = tkinter.Label(window,text="T",font = ("arial",15,"bold"))
                token1.grid(row = row_coordinates[a] , column = column_coordinates[a])
                my_places.update({a:"occupied"})"""


root.mainloop()

# token1 = tkinter.Label(root, text="T", font=("arial", 15, "bold"))
# token1.grid(row=row_coordinates[a], column=column_coordinates[a])
#my_places.update({a: "occupied"})
# tokens[chance] = {"position":[row_coordinates[position],column_coordinates[position]]}
# MAKE CHANGES HERE WHILE MAKING SAVE FEATURE
#AttributeError: 'NoneType' object has no attribute 'grid'