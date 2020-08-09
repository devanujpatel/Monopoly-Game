import tkinter

window = tkinter.Tk()

#left column
tkinter.Frame(window, width=150, height=60, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=2, column=0)
tkinter.Frame(window, width=150, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=3, column=0)
tkinter.Frame(window, width=150, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=4, column=0)
tkinter.Frame(window, width=150, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=5, column=0)
tkinter.Frame(window, width=150, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=6, column=0)
tkinter.Frame(window, width=150, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=7, column=0)
tkinter.Frame(window, width=150, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=8, column=0)
tkinter.Frame(window, width=150, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=9, column=0)
tkinter.Frame(window, width=150, height=60, bg="green", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=10, column=0)

# upper row lane
tkinter.Frame(window, width=150, height=115, relief=tkinter.RIDGE, bg="orange", highlightbackground="black",
              highlightthickness=1).grid(row=1, column=0)
tkinter.Frame(window, width=110, height=115, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=1)
tkinter.Frame(window, width=110, height=115, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=2)
tkinter.Frame(window, width=110, height=115, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=3)
tkinter.Frame(window, width=110, height=115, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=4)
tkinter.Frame(window, width=110, height=115, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=5)
tkinter.Frame(window, width=110, height=115, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=6)
tkinter.Frame(window, width=110, height=115, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=7)
tkinter.Frame(window, width=110, height=115, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=8)
tkinter.Frame(window, width=110, height=115, bg="blue", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=9)
tkinter.Frame(window, width=150, height=115, bg="yellow", relief=tkinter.RIDGE, highlightbackground="black",
              highlightthickness=1).grid(row=1, column=10)

# right column lane excluding
tkinter.Frame(window, width=150, height=60, relief=tkinter.RIDGE, bg="black", highlightbackground="black",
              highlightthickness=1).grid(row=2, column=10)
tkinter.Frame(window, width=150, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=3, column=10)
tkinter.Frame(window, width=150, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=4, column=10)
tkinter.Frame(window, width=150, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=5, column=10)
tkinter.Frame(window, width=150, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=6, column=10)
tkinter.Frame(window, width=150, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=7, column=10)
tkinter.Frame(window, width=150, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=8, column=10)
tkinter.Frame(window, width=150, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=9, column=10)
tkinter.Frame(window, width=150, height=60, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=10, column=10)

#lower lane
just = tkinter.Frame(window, width=150, height=115, bg="pink", relief=tkinter.RIDGE, highlightbackground="black",
                     highlightthickness=1).grid(row=11, column=0)
tkinter.Frame(window, width=110, height=115, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=1)
tkinter.Frame(window, width=110, height=115, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=2)
tkinter.Frame(window, width=110, height=115, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=3)
tkinter.Frame(window, width=110, height=115, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=4)
tkinter.Frame(window, width=110, height=115, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=5)
tkinter.Frame(window, width=110, height=115, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=6)
tkinter.Frame(window, width=110, height=115, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=7)
tkinter.Frame(window, width=110, height=115, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=8)
tkinter.Frame(window, width=110, height=115, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=9)
go_box = tkinter.Frame(window, width=150, height=115, relief=tkinter.RIDGE, bg="brown", highlightbackground="black",
                       highlightthickness=1).grid(row=11, column=10)
