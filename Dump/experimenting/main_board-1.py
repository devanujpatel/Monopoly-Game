
import tkinter
import keyboard
from PIL import ImageTk,Image
window = tkinter.Tk()

keyboard.add_hotkey('shift+z', lambda: roll_dice())
monopoly_display = tkinter.Label(window,text = "MONOPOLY",bg = "brown" , fg = "white",font=("Times New Roman",18,"bold" ))
monopoly_display.place(relx = 0.5 , rely = 0.5 , anchor="center")
roll_dice_button = tkinter.Button(window,text = "Roll Dice",bg = "orange",fg = "black",command = lambda:roll_dice(),width=18,height=3)
roll_dice_button.place(relx = 0.5, rely = 0.5, x = 40,y = 60)

tkinter.Frame(window,width = 140,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=2,column=0)
mediteranean_avenue =tkinter.Frame(window,width = 140,height = 60,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=4,column=0)
community1 =tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=6,column=0)
baltic_avenue = tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=8,column=0)
income_tax = tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=10,column=0)
reading_railroad = tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=12,column=0)
oriental_avenue = tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=14,column=0)
chance1 = tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=16,column=0)
vermount_avenue = tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=18,column=0)
connecticut_avenue = tkinter.Frame(window,width = 140,height = 60,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=20,column=0)
just_visiting = tkinter.Frame(window,width = 140,height = 80,bg = "green",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=22,column=0)

st_charles_place = tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=1)
electric_company = tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=3)
states_avenue = tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=5)
virginia_avenue = tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=7)
pensilvania_railroad = tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=9)
st_james_place = tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=11)
community_chest_2 = tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=13)
tennesse_avenue = tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=15)
new_york_avenue = tkinter.Frame(window,width = 120,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=17)
free_parking = tkinter.Frame(window,width = 140,height = 80,bg = "blue",relief = tkinter.RIDGE,highlightbackground = "black",highlightthickness=1).grid(row=2,column=19)

kentucky_avenue = tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=4,column=19)
indiana_avenue= tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row = 6 ,column=19)
chance_2 = tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=8,column=19)
illinois_avenue = tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=10,column=19)
b_and_o_railway = tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=12,column=19)
atlantic_avenue = tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=14 , column=19)
ventnor_avenue = tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=16 , column=19)
water_works = tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=18,column=19)
marvin_gardens = tkinter.Frame(window,width = 140,height = 60,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=20,column=19)
go_to_jail = tkinter.Frame(window,width = 140,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=19)

pacific_avenue = tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=1)
north_caroline_avenue = tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=3)
chance_3 = tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=5)
short_line = tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=7)
pensylvania_avenue = tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=9)
community_3= tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=11)
north_caroline_avenue = tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=13)
pacific_avenue = tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=15)
go_to_jail = tkinter.Frame(window,width = 120,height = 80,relief = tkinter.RIDGE,bg = "pink",highlightbackground = "black",highlightthickness=1).grid(row=22,column=17)



"""deathwing = Image.open('monopoly board.jpg')
image2 = deathwing.resize((1000, 700), Image.ANTIALIAS)
Deathwing2 = ImageTk.PhotoImage(image2)
tkinter.Label(window,image = Deathwing2).place(x=180,y=7)
"""
import random


position = 0

def roll_dice():

    global position
    dice_val = random.randint(1,7)
    position += dice_val
    move_token()


my_places ={'go_box':" ",'mediteranean_avenue':" ",'community1' :" ",'baltic_avenue':" ",'income_tax':" ",'reading_railroad' :" ",'oriental_avenue':" ",'chance1':" ",'vermount_avenue':" ",'connecticut_avenue':" ",'just_visiting':" ",}
row_coordinates= {}
column_coordinates = {}
myplace_num ={}
myplaces=[]

for place in my_places.keys():
    myplaces.append(str(place))

d = 2
for pl in my_places.keys():
    column_coordinates.update({pl:0})
    row_coordinates.update({pl:d})
    d += 2

i = 0
for p in myplaces:
    myplace_num.update({p:i})
    i += 1

token1 = tkinter.Label(window,text="T",bg = "white",fg = "black",font = ("arial",20,"bold")).grid(row=2,column=0)

last_pos  = []

def move_token():
        global token1
        for a in myplaces:
            if position == myplace_num[a]:
                token1 = tkinter.Label(window,text="   ").grid(row=2,column=0)
                token1 = tkinter.Label(window,text="T",font = ("arial",15,"bold")).grid(row = row_coordinates[a] , column = column_coordinates[a])
                my_places.update({a:"occupied"})




window.mainloop()