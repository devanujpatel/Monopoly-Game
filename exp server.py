import pickle
import socket

s = socket.socket()
s.bind(("localhost",9999))
s.listen(1)

func = pickle.dumps("hey(4)")

sockets = []
while True:
    client, addr = s.accept()
    client.send(bytes("hi there!",'utf-8'))
    sockets.append(client)
