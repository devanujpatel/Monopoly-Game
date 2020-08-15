#1366 768

# max height = 660
# max width = 1640

"""To add a hotkey:
import keyboard
keyboard.add_hotkey('shift+z', lambda: roll_dice())"""

#position = (1307,721)
#(182, 102) left corner of inner rectangle
"""
# left column lane excluding 1st and last cell
tkinter.Frame(window, width=140, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=2, column=0)
tkinter.Frame(window, width=140, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=3, column=0)
tkinter.Frame(window, width=140, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=4, column=0)
tkinter.Frame(window, width=140, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=5, column=0)
tkinter.Frame(window, width=140, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=6, column=0)
tkinter.Frame(window, width=140, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=7, column=0)
tkinter.Frame(window, width=140, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=8, column=0)
tkinter.Frame(window, width=140, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=9, column=0)
tkinter.Frame(window, width=140, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=10, column=0)

# upper row lane
tkinter.Frame(window, width=140, height=80, relief=tkinter.RIDGE, bg="orange", highlightbackground="black",
              highlightthickness=1).grid(row=1, column=0)
tkinter.Frame(window, width=120, height=80, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=1)
tkinter.Frame(window, width=120, height=80, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=2)
tkinter.Frame(window, width=120, height=80, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=3)
tkinter.Frame(window, width=120, height=80, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=4)
tkinter.Frame(window, width=120, height=80, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=5)
tkinter.Frame(window, width=120, height=80, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=6)
tkinter.Frame(window, width=120, height=80, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=7)
tkinter.Frame(window, width=120, height=80, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=8)
tkinter.Frame(window, width=120, height=80, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=9)
tkinter.Frame(window, width=140, height=80, bg="yellow", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=10)

# right column lane excluding
tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="black", highlightbackground="black",
              highlightthickness=1).grid(row=2, column=10)
tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=3, column=10)
tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=4, column=10)
tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=5, column=10)
tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=6, column=10)
tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=7, column=10)
tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=8, column=10)
tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=9, column=10)
tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=10, column=10)

# lower row lane
just = tkinter.Frame(window, width=140, height=80, bg="pink", relief=tkinter.RIDGE, highlightbackground="black",
                     highlightthickness=1).grid(row=11, column=0)
tkinter.Frame(window, width=120, height=80, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=1)
tkinter.Frame(window, width=120, height=80, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=2)
tkinter.Frame(window, width=120, height=80, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=3)
tkinter.Frame(window, width=120, height=80, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=4)
tkinter.Frame(window, width=120, height=80, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=5)
tkinter.Frame(window, width=120, height=80, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=6)
tkinter.Frame(window, width=120, height=80, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=7)
tkinter.Frame(window, width=120, height=80, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=8)
tkinter.Frame(window, width=120, height=80, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=9)
go_box = tkinter.Frame(window, width=140, height=80, relief=tkinter.RIDGE, bg="brown", highlightbackground="black",
                       highlightthickness=1).grid(row=11, column=10)


winfo_screenheight() // Returns screen height in pixels

winfo_screenmmheight() // Returns screen height in mm

winfo_screenwidht() // Returns screen width in pixels"""


"""in=
Place widget inside to the given widget. You can only place a widget inside its parent, or in any decendant of its parent. If this option is not given, it defaults to the parent.

Note that in is a reserved word in Python. To use it as a keyword option, append an underscore (in_).

in_=
Same as in. See above.
ipadx=
Optional horizontal internal padding. Works like padx, but the padding is added inside the widget borders. Default is 0.
ipady=
Optional vertical internal padding. Works like pady, but the padding is added inside the widget borders. Default is 0.
padx=
Optional horizontal padding to place around the widget in a cell. Default is 0.
pady=
Optional vertical padding to place around the widget in a cell. Default is 0."""



