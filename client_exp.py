"""import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9999))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg.decode("utf-8")

        print(len(full_msg))


        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = """""
import socket
s = socket.socket()
s.connect(("127.0.0.1",9999))

while True:
    msg = s.recv(24)
    msg = msg.decode('utf-8')
    print(msg)
