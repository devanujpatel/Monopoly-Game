
import tkinter
import keyboard
from PIL import ImageTk,Image
window = tkinter.Tk()

deathwing = Image.open('monopoly board.jpg')
image = deathwing
#deathwing.ImageTk.PhotoImage()
#image2 = deathwing.resize((1000, 700), Image.ANTIALIAS)
Deathwing2 = ImageTk.PhotoImage(image)

keyboard.add_hotkey('shift+z', lambda: roll_dice())
monopoly_display = tkinter.Label(window,text = "MONOPOLY",bg = "brown" , fg = "white",font=("Times New Roman",18,"bold" ))
monopoly_display.place(relx = 0.5 , rely = 0.5 , anchor="center")
roll_dice_button = tkinter.Button(window,text = "Roll Dice",bg = "orange",fg = "black",command = lambda:roll_dice(),width=18,height=3)
roll_dice_button.place(relx = 0.5, rely = 0.5, x = 40,y = 60)

"""
# left column lane excluding 1st and last cell
tkinter.Frame(window,width = 140,height = 60,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=0)
tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=3,column=0)
tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=4,column=0)
tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=5,column=0)
tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=6,column=0)
tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=7,column=0)
tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=8,column=0)
tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=9,column=0)
tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=10,column=0)

# upper row lane
tkinter.Frame(window,width = 140,height = 80,relief = tkinter.RIDGE,bg = "orange",highlightbackground = "black",highlightthickness=1).grid(row=1,column=0)
tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=1,column=1)
tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=1,column=2)
tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=1,column=3)
tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=1,column=4)
tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=1,column=5)
tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=1,column=6)
tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=1,column=7)
tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=1,column=8)
tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=1,column=9)
tkinter.Frame(window,width = 140,height = 80,bg = "yellow",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=1,column=10)

# right column lane excluding
tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "black",highlightbackground = "black",highlightthickness=1).grid(row=2,column=10)
tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row =3 ,column=10)
tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=4,column=10)
tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=5,column=10)
tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=6,column=10)
tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=7 , column=10)
tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=8 , column=10)
tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=9,column=10)
tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=10,column=10)

# lower row lane
just = tkinter.Frame(window,width = 140,height = 80,bg = "pink",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=22,column=0)
tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=1)
tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=2)
tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=3)
tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=4)
tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=5)
tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=6)
tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=7)
tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=8)
tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=9)
go_box = tkinter.Frame(window,width = 140,height = 80,relief = tkinter.RIDGE,bg = "brown",highlightbackground = "black",highlightthickness=1).grid(row=22,column=10)
"""
import random

position = 0

def roll_dice():

    global position,dice_val
    dice_val = random.randint(1,6)
    position += dice_val
    show_dice = tkinter.StringVar()
    label_dice = "Dice Roll = "+str(dice_val)
    show_dice.set(label_dice)
    tkinter.Label(window,textvariable=show_dice,bg="green",fg="orange",width=12,height=3).place(relx = 0.5, rely = 0.5, x = 80,y = 8)
    if position >=41:
        position = position - 41


    move_token()


my_places ={'go_box':" ",'mediteranean_avenue':" ",'community1' :" ",'baltic_avenue':" ",'income_tax':" ",
            'reading_railroad' :" ",'oriental_avenue':" ",'chance1':" ",'vermount_avenue':" "
            ,'connecticut_avenue':" ",'just_visiting':" "
    ,'st_charles_place':" ",'electric_company':" ",'states_avenue':" ",'virginia_avenue':" ",
            'pennsylvania_railroad':" ",'st_james_place':" ",'community2':" ",'tennessesse_avenue':" ",'new_york_avenue':" "
        ,'free_parking':" ",'kentucky_avenue':" ",'chance2':" ",'india_avenue':" ",'illinois_avenue':" ",'b_and_o_railroad':" ",'atlantic_avenue':" ",'ventnor_avenue':" ",
            'water_works':" ",'marvin_gardens':" ",'go_to_jail':" ",
        'pacific_avenue':" ",'north_carolina_avenue':" ",'community3':" ",'pennsylvania_avenue':" ",
            'shortline':" ",'chance3':" ",'park_place':" ",'luxury_tax':" ",'board_walk':" "}

row_coordinates= {}
column_coordinates = {}
myplace_num ={}
myplaces=[]

for place in my_places.keys():
    myplaces.append(str(place))

# go till jail
c1 = 10
for pl in myplaces[0:12]:
    column_coordinates.update({pl: c1})
    row_coordinates.update({pl:22})
    c1 -= 1

# st_charles till new york avenue
r1 = 10
for pl in myplaces[11:20]:
    column_coordinates.update({pl:0})
    row_coordinates.update({pl:r1})
    r1 -= 1

# free parking till go to jail
c2 = 0
for pl in myplaces[20:32]:
    column_coordinates.update({pl: c2})
    row_coordinates.update({pl:1})
    c2 += 1

# pacific till board walk
r2 = 2
for pl in myplaces[32:41]:
    column_coordinates.update({pl:10})
    row_coordinates.update({pl:r2})
    r2 += 1


print(row_coordinates)

print(column_coordinates)

i = 0
for p in myplaces:
    myplace_num.update({p:i})
    i += 1

def show():
    global token1
    token1 = tkinter.Label(window, text="T", bg="white", fg="black", font=("arial", 20, "bold"))
    token1.grid(row=22, column=10)

def forget_widget():

    token1.grid_forget()

show()

def show_diceroll():
    global dice_val
    print("dice roll:",str(dice_val))
    print("position:",str(position))

def move_token():
        global token1
        for a in myplaces:
            if position == myplace_num[a]:
                forget_widget()
                token1 = tkinter.Label(window,text="T",font = ("arial",15,"bold"))
                token1.grid(row = row_coordinates[a] , column = column_coordinates[a])
                my_places.update({a:"occupied"})

window.mainloop()