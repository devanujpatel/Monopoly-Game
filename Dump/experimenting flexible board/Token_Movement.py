from Monopoly_Board import *

import random

monopoly_display = tkinter.Label(window, text="MONOPOLY", bg="brown", fg="white", font=("Times New Roman", 18, "bold"))
monopoly_display.place(relx=0.5, rely=0.5, anchor="center")

roll_dice_button = tkinter.Button(window, text="Roll Dice", bg="orange", fg="black", command=lambda: roll_dice(),
                                  width=18, height=3)
roll_dice_button.place(relx=0.5, rely=0.5, x=40, y=60)

position = 0

def roll_dice():
    global position, dice_val
    dice_val = random.randint(1, 6)
    position += dice_val
    show_dice = tkinter.StringVar()
    label_dice = "Dice Roll = " + str(dice_val)
    show_dice.set(label_dice)
    tkinter.Label(window, textvariable=show_dice, bg="green", fg="orange", width=12, height=3).place(relx=0.5, rely=0.5,
                                                                                                     x=80, y=8)
    if position >= 40:
        position = position - 40

    move_token()


my_places = {'go_box': " ", 'mediteranean_avenue': " ", 'community1': " ", 'baltic_avenue': " ", 'income_tax': " ",
             'reading_railroad': " ", 'oriental_avenue': " ", 'chance1': " ", 'vermount_avenue': " "
    , 'connecticut_avenue': " ", 'just_visiting': " "
    , 'st_charles_place': " ", 'electric_company': " ", 'states_avenue': " ", 'virginia_avenue': " ",
             'pennsylvania_railroad': " ", 'st_james_place': " ", 'community2': " ", 'tennessesse_avenue': " ",
             'new_york_avenue': " "
    , 'free_parking': " ", 'kentucky_avenue': " ", 'chance2': " ", 'india_avenue': " ", 'illinois_avenue': " ",
             'b_and_o_railroad': " ", 'atlantic_avenue': " ", 'ventnor_avenue': " ",
             'water_works': " ", 'marvin_gardens': " ", 'go_to_jail': " ",
             'pacific_avenue': " ", 'north_carolina_avenue': " ", 'community3': " ", 'pennsylvania_avenue': " ",
             'shortline': " ", 'chance3': " ", 'park_place': " ", 'luxury_tax': " ", 'board_walk': " "}

row_coordinates = {}
column_coordinates = {}
myplace_num = {}
myplaces = []

for place in my_places.keys():
    myplaces.append(str(place))

# go till jail
c1 = 10
for pl in myplaces[0:11]:  # changed 12 to 11
    column_coordinates.update({pl: c1})
    row_coordinates.update({pl: 11})
    c1 -= 1

# st_charles till new york avenue
r1 = 10
for pl in myplaces[11:20]:
    column_coordinates.update({pl: 0})
    row_coordinates.update({pl: r1})
    r1 -= 1

# free parking till go to jail
c2 = 0
for pl in myplaces[20:31]:  # changed 32 to 31
    column_coordinates.update({pl: c2})
    row_coordinates.update({pl: 1})
    c2 += 1

# pacific till board walk
r2 = 2
for pl in myplaces[31:40]:
    column_coordinates.update({pl: 10})
    row_coordinates.update({pl: r2})
    r2 += 1

i = 0
for p in myplaces:
    myplace_num.update({p: i})
    i += 1

def forget_widget(widget):

    widget.grid_forget()

update_tokens = False

def move_token():
    global token1,update_tokens

    for a in myplaces:
        if position == myplace_num[a]:
            update_tokens = True

window.mainloop()

# token1 = tkinter.Label(window, text="T", font=("arial", 15, "bold"))
# token1.grid(row=row_coordinates[a], column=column_coordinates[a])
#my_places.update({a: "occupied"})
