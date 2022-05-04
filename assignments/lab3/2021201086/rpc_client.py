import socket
PORT = 9000
SERVER = socket.gethostbyname((socket.gethostname()))
ADDRESS = (SERVER, PORT)
MAX_sIZE = 600

def rpc_connector(func_name, param_list):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDRESS)
	func_dict_str = str({func_name: param_list}).encode()
	client.send(func_dict_str)
	func_ret = client.recv(MAX_sIZE).decode()
	return func_ret


def foo(par_1:str):
	return str(rpc_connector('foo',[par_1]))


def bar(par_1:int,par_2:float):
	return float(rpc_connector('bar',[par_1,par_2]))


def zoo():
	return str(rpc_connector('zoo',[]))


def boo(par_1:float):
	rpc_connector('boo',[par_1])

