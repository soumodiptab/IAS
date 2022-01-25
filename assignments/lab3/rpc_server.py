import socket
import threading
from server_procedures import *

PORT = 9000
SERVER = socket.gethostbyname((socket.gethostname()))
ADDRESS = (SERVER, PORT)
MAX_sIZE = 600
STATUS_CODES = {"SUCCESS": 0, "FAIL": 1}


def caller(func_dict):
    fname = list(func_dict.keys())[0]
    arguments = func_dict[fname]
    function_call = f"{fname}(*{arguments})"
    ret_value = eval(function_call)
    return ret_value


def rpc_handler(conn):
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
    try:
        server.listen()
        while True:
            conn, addr = server.accept()
            new_thread = threading.Thread(target=rpc_handler, args=(conn,))
            new_thread.start()
    except KeyboardInterrupt:
        print("RPC SERVER is closing down")
        server.close()
        exit()


start()
