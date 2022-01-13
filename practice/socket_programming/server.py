import socket
import threading
HEADER = 64
PORT = 5050
DISCONNECT_MSG = "DISCONNECT"
SERVER = socket.gethostbyname((socket.gethostname()))
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def client_thread(conn, addr):
    print(f"[INFO]{addr} connected")
    connected = True
    while connected:
        # decode the message from byte format
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
        print(f"[INFO]{addr} : {msg}")
    conn.close()


def start():
    server.listen()
    while True:
        # When a new connection gets accepted it passes the obj to conn,addr
        conn, addr = server.accept()
        # conn: same as opening a socket file
        new_thread = threading.Thread(target=client_thread, args=(conn, addr))
        new_thread.start()
        print(f"[INFO] Active conn.s :{threading.activeCount()-1}")


print("[INFO]Starting server...")
start()
