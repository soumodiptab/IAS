import socket
import threading
PORT = 5050
DISCONNECT_MSG = "DISCONNECT"
SERVER = socket.gethostbyname((socket.gethostname()))
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
def make_server(conn,addr):
    
def make_client(conn,addr):

def start_client(addr_client,addr_server):


def start():
    choice=input('Start C1 or C2 ?\n')
    if choice == 'C1':
