
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.29.201" , 9999))
s.listen(5)
print(" I am listening")

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hi! good to see you!!!","utf-8"))
    clientsocket.close()

