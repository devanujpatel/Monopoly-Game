# this is the file of our tkinter version of displaying our board

import tkinter

window = tkinter.Tk()

monopoly_display = tkinter.Label(window, text="MONOPOLY", bg="brown", fg="white", font=("Times New Roman", 18, "bold"))
monopoly_display.place(relx=0.5, rely=0.5, anchor="center")

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
tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="orange", highlightbackground="black",
              highlightthickness=1).grid(row=1, column=0)
tkinter.Frame(window, width=120, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=1)
tkinter.Frame(window, width=120, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=2)
tkinter.Frame(window, width=120, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=3)
tkinter.Frame(window, width=120, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=4)
tkinter.Frame(window, width=120, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=5)
tkinter.Frame(window, width=120, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=6)
tkinter.Frame(window, width=120, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=7)
tkinter.Frame(window, width=120, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=8)
tkinter.Frame(window, width=120, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=9)
tkinter.Frame(window, width=140, height=60, bg="yellow", relief=tkinter.RIDGE, highlightbackground="black",
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
just = tkinter.Frame(window, width=140, height=60, bg="pink",relief=tkinter.RIDGE, highlightbackground="black",
                     highlightthickness=1).grid(row=11, column=0)
#text = tkinter.Label(just,text="Dev Hemkesh").grid(row= 1, column=10 , sticky="n")
tkinter.Frame(window, width=120, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=1)
tkinter.Frame(window, width=120, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=2)
tkinter.Frame(window, width=120, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=3)
tkinter.Frame(window, width=120, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=4)
tkinter.Frame(window, width=120, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=5)
tkinter.Frame(window, width=120, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=6)
tkinter.Frame(window, width=120, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="blue",
              highlightthickness=1).grid(row=11, column=7)
tkinter.Frame(window, width=120, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=8)
tkinter.Frame(window, width=120, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=9)
go_box = tkinter.Frame(window, width=140, height=60, relief=tkinter.RIDGE, bg="brown", highlightbackground="yellow",
                       highlightthickness=1).grid(row=11, column=10)