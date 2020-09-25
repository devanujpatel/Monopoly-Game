import tkinter
import time
root = tkinter.Tk()

width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight() # height of screen

root.geometry("%dx%d%+d%+d" % (width, height, 0 ,0))
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


# NOT HAPPENING: ENJOY LABEL IS NOT GETTING DISPLAYED!!!☺
"""enjoy_widget = tkinter.Label(root, text="ENJOY!", bg="orange",width=40,height=20, fg="black")
def show_enjoy():
    time.sleep(0.4)
    enjoy_widget.grid(row=6,column=5)
    time.sleep(1)
    enjoy_widget.grid_forget()"""




"""def move_token():
    global token1,update_tokens

    for a in myplaces:
        if position == myplace_num[a]:
            update_tokens = True
"""





"""if go_ahead == True:
    allow = True
else:
    allow = False"""