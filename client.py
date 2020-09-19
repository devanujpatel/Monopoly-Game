import socket
import threading
from queue import Queue
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("192.168.29.201",9999))
    print("Connection established server!")
except error as e:
    print("Some error occured while connecting to the server.",e)
    s.close()
   
username = input("Enter your username: ")

while True:
    break

