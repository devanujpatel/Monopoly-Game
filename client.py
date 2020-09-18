import socket
import tkinter as tk

client = socket.socket()
client.connect(("127.0.01",9999))

container = tk.Tk()

# setting width and height of tkinter window so as to fit screen!
width = container.winfo_screenwidth()  # width of screen
height = container.winfo_screenheight()  # height of screen

container.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

start_frame= tk.Frame(container, width=width, height=height)
start_frame.grid(row=0, column=0, sticky="nsew")

# make a grid on the container so as to make placing easier

for row in range(5):
    for col in range(5):
        tk.Frame(start_frame).grid(row= row, colmun = col)

font = ("Courier", 13)
username_entry = tk.Entry(start_frame)
ok_but_for_username = tk.Button(start_frame, text= "Okay",font= font,command= lambda :ok_but_for_username_clicked)
username_entry.grid(row=3,column=3)
ok_but_for_username.grid(row=4,column=3)

def ok_but_for_username_clicked():
    ok_but_for_username.grid_forget()
    username = username_entry.get()

    if username == "":
        ok_but_for_username.grid(row=4,column=3)

    else:
        username_entry.grid_forget()

    client.send(bytes(username,'utf-8'))
