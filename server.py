import socket
import threading
import tkinter as tk

# create our server socket : defaults to AF_INET and streaming socket!
server = socket.socket()
server.bind(("",9999))
server.listen()


# start new thread for recieving username and etc stuff (this will also be the thread which will handle the game for the player)
class Client(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)

    def run(self):
        # recv username , new room or join room , favourite color, etc...
        # do further things like waiting or playing






while True:
    client, addr = server.accept()
    # creating obj of Client hope it overwrites the obj name everytime a new player joins
    thread = Client(client, addr)
    thread.start()



