import socket
PORT = 5000
SERVER = socket.gethostbyname((socket.gethostname()))
ADDRESS = (SERVER, PORT)


def rpc_connector(func_name, param_list):
    print("connecting to server")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    func_dict_str = str({func_name: param_list}).encode()
    client.send(func_dict_str)
    func_ret = client.recv(600).decode()
    return func_ret


def foo(param1):
    return str(rpc_connector('foo', [param1]))


def bar(param1, param2):
    return float(rpc_connector('bar', [param1, param2]))
