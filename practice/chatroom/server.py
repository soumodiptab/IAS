import socket
import sys
from thread import *

ip, port = ('127.0.0.1', 4000)
# server socket IPV4 family , Continous socket stream
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print("Invalid arguments... using default")
else:
    ip = str(sys.argv[1])
    port = int(sys.argv[2])
# takes the first argument from command prompt as IP address
server.bind(ip, port)
#listen to 100 active connections
server.listen(100)
list_of_clients = []
def client_thread(connection,address):
    print('hello new client')
