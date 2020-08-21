import tkinter

"""class seaofplace(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args , **kwargs)
        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.width = container.winfo_screenwidth()  # width of screen
        self.height = container.winfo_screenheight()  # height of screen

        container.winfo_toplevel().geometry("%dx%d%+d%+d" % (self.width, self.height, 0, 0))

        main_place = tkinter.Frame(container, bg="red")
        main_place.grid()

        place = tkinter.Label(main_place, text="place1")
        place.pack()

        place2 = tkinter.Label(main_place, text="place2")
        place2.pack()"""

root = tkinter.Tk()

m = tkinter.Frame(root, bg="red" ,width = 500 , height=500)
m.grid(row=-0,column=0)

r = tkinter.Frame(root, bg="orange",width = 500 , height=500)
m.grid(row=1,column=0)

q = tkinter.Label(m, bg="blue")
q.pack()

w =  tkinter.Label(m, bg="orange")
w.pack()

root.mainloop()

"""
        place1 = tkinter.Label(main_place, bg="orange", width=2, height=1)
        place1.place(relx=0.4, rely=0.7)

        place2 = tkinter.Label(main_place, bg="orange", width=2, height=1)
        place2.place(relx=0.1, rely=0.7)

        place3 = tkinter.Label(main_place, bg="orange", width=2, height=1)
        place3.place(relx=0.7, rely=0.7)

        place2 = tkinter.Label(main_place, bg="blue", width=2, height=1)
        place2.place(relx=0.1, rely=0.4)

        place1 = tkinter.Label(main_place,text="bo rail", bg="white")
        place1.place(relx=0.4, rely=0.4)

        place3 = tkinter.Label(main_place, bg="blue", width=2, height=1)
        place3.place(relx=0.7, rely=0.4)

        place1 = tkinter.Label(main_place, bg="light green", width=2, height=1)
        place1.place(relx=0.4, rely=0.1)

        place2 = tkinter.Label(main_place, bg="light green", width=2, height=1)
        place2.place(relx=0.1, rely=0.1)

        place3 = tkinter.Label(main_place, bg="light green", width=2, height=1)
        place3.place(relx=0.7, rely=0.1)

    def small_box(self):
                container = tkinter.Frame(self)
                container.pack(side="top", fill="both", expand=True)
                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)

                self.width = container.winfo_screenwidth()  # width of screen
                self.height = container.winfo_screenheight()  # height of screen

                container.winfo_toplevel().geometry("%dx%d%+d%+d" % (self.width, self.height, 0, 0))

                main_place = tkinter.Frame(container, width=116, height=47, bg="red")
                main_place.pack(side="top")

                place1 = tkinter.Label(main_place, bg="orange", width=2, height=1)
                place1.place(relx=0.4, rely=0.7)

                place2 = tkinter.Label(main_place, bg="orange", width=2, height=1)
                place2.place(relx=0.1, rely=0.7)

                place3 = tkinter.Label(main_place, bg="orange", width=2, height=1)
                place3.place(relx=0.7, rely=0.7)

                place2 = tkinter.Label(main_place, bg="blue", width=2, height=1)
                place2.place(relx=0.1, rely=0.4)

                place1 = tkinter.Label(main_place, text="bo rail", bg="white")
                place1.place(relx=0.4, rely=0.4)

                place3 = tkinter.Label(main_place, bg="blue", width=2, height=1)
                place3.place(relx=0.7, rely=0.4)

                place1 = tkinter.Label(main_place, bg="light green", width=2, height=1)
                place1.place(relx=0.4, rely=0.1)

                place2 = tkinter.Label(main_place, bg="light green", width=2, height=1)
                place2.place(relx=0.1, rely=0.1)

                place3 = tkinter.Label(main_place, bg="light green", width=2, height=1)
                place3.place(relx=0.7, rely=0.1)
                """

"""

obj = seaofplace()
#obj.small_box()
obj.mainloop()"""