import pickle
import socket

s = socket.socket()
s.connect(('127.0.0.1',9999))

def hey(n):
    return "in client",n

func = s.recv(1024)
func = pickle.loads(func)
print(func)
