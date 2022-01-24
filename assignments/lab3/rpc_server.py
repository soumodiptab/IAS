import socket
import ast
import threading
from server_procedures import *

PORT = 9000
SERVER = socket.gethostbyname((socket.gethostname()))
ADDRESS = (SERVER, PORT)
MAX_sIZE = 600

def caller(func_dict):
	fname = list(func_dict.keys())[0]
	arguments = func_dict[fname]
	if fname == 'foo':
		return foo(*arguments)
	elif fname == 'bar':
		return bar(*arguments)
	elif fname == 'zoo':
		return zoo(*arguments)
	elif fname == 'boo':
		return boo(*arguments)
	else:
		return "Invalid"

def rpc_handler(conn, addr):
    function_info = conn.recv(MAX_sIZE).decode()
    func_dict = eval(function_info)
    print("RPC REQUEST: ")
    print(func_dict)
    ret_value = caller(func_dict)
    print(f"RPC REPLY:{ret_value}")
    conn.send(str(ret_value).encode())
    conn.close()

def start():
    print("RPC SERVER has started")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen()
    while True:
        conn, addr = server.accept()
        new_thread = threading.Thread(target=rpc_handler, args=(conn, addr))
        new_thread.start()
start()
