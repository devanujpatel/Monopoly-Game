import socket
import tkinter as tk

root = tk.Tk()
# setting width and height of tkinter window so as to fit screen!
width = root.winfo_screenwidth()  # width of screen
height = root.winfo_screenheight()  # height of screen

root.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

start_frame= tk.Frame(root, width=width, height=height)
start_frame.grid(row=0, column=0, sticky="nsew")

# make a grid on the root so as to make placing easier

for row in range(5):
    for col in range(5):
        tk.Frame(start_frame).grid(row= row, column = col)

font = ("Courier", 13)
username_entry = tk.Entry(start_frame)
ok_but_for_username = tk.Button(start_frame, text= "Okay",font= font,command= lambda :ok_but_for_username_clicked())
username_entry.grid(row=3,column=3)
ok_but_for_username.grid(row=4,column=3)

def ok_but_for_username_clicked():
    print("okay button clicked")
    ok_but_for_username.grid_forget()
    username = username_entry.get()

    if username == "":
        ok_but_for_username.grid(row=4,column=3)

    else:
        username_entry.grid_forget()

        client = socket.socket()
        client.connect(('127.0.0.1', 9999))
        HEADER = 10
        send_username = f"{len(username):<{HEADER}}" + username
        client.send(bytes(send_username,'utf-8'))
        msg_length = client.recv(HEADER)
        msg_length = int(msg_length.decode('utf-8'))
        msg = client.recv(msg_length)
        print(msg)
        false = "false"
        client.send(bytes(false,'utf-8'))

        hey = client.recv(16)
        hey = hey.decode('utf-8')
        print(hey)

root.mainloop()