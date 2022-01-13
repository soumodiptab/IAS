import threading
import socket
HEADER = 64
DISCONNECT_MSG = "DISCONNECT"
PORT = 5050
SERVER = socket.gethostbyname((socket.gethostname()))
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'


def start():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    connected = True
    while connected == True:
        print("<<")
        message = input()
        message =  b"HTTP/1.1 200 OK\n\n"+message
        msg = message.encode(FORMAT)
        msg_length = len(message)
        length = str(msg_length).encode(FORMAT)
        length += b' '*(HEADER - len(length))
        client.send(length)
        client.send(msg)
        # print(client.recv(2048).decode())


print("[INFO]Starting client...")
start()
