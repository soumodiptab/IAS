from distutils.errors import LibError
import json
# --Configuration-----------------
FILE_NAME = 'rpc_server.py'
SERVER = '127.0.0.1'
PORT = 9000
INDENT = '\t'
LINE_END = '\n'
# --------------------------------


def json_loader(file):
    g = open(file)
    data = json.load(g)
    g.close()
    return data


imports = ["socket", "threading"]

config = {
    "PORT": PORT,
    "SERVER": "socket.gethostbyname((socket.gethostname()))",
    "ADDRESS": "(SERVER, PORT)",
    "MAX_sIZE": "600"
}


def import_generator():
    out_string = ""
    for imp in imports:
        out_string = out_string+f"import {imp}"+LINE_END
    out_string = out_string+"from server_procedures import *"+LINE_END
    return out_string+LINE_END


def config_generator():
    out_string = ""
    for c in config.keys():
        out_string = out_string+f"{c} = {config[c]}"+LINE_END
    return out_string+LINE_END


def rpc_builder():
    out_string = '''def rpc_handler(conn):
    function_info = conn.recv(MAX_sIZE).decode()
    func_dict = eval(function_info)
    print("RPC REQUEST: ")
    print(func_dict)
    ret_value = caller(func_dict)
    print(f"RPC REPLY:{ret_value}")
    conn.send(str(ret_value).encode())
    conn.close()'''+LINE_END+LINE_END
    return out_string


def app_start_builder():
    out_string = '''def start():
    print("RPC SERVER has started")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    try:
        server.listen()
        while True:
            conn, addr = server.accept()
            new_thread = threading.Thread(target=rpc_handler, args=(conn, addr))
            new_thread.start()
    except KeyboardInterrupt:
        print("RPC SERVER is closing down")
        server.close()
        exit()'''+LINE_END+LINE_END+"start()"+LINE_END
    return out_string


def function_name(procedure):
    function_name = procedure["procedure_name"]
    return function_name


def caller_builder(procedures):
    out_string = "def caller(func_dict):"+LINE_END +\
        INDENT+"fname = list(func_dict.keys())[0]"+LINE_END +\
        INDENT+"arguments = func_dict[fname]"+LINE_END
    number = len(procedures)
    if number == 0:
        return out_string+INDENT+'return "Invalid"'
    i = 0
    out_string += INDENT+f"if fname == '{function_name(procedures[i])}':"+LINE_END +\
        INDENT+INDENT + \
        f"return {function_name(procedures[i])}(*arguments)"+LINE_END
    i += 1
    while i < number:
        out_string += INDENT+f"elif fname == '{function_name(procedures[i])}':"+LINE_END +\
            INDENT+INDENT + \
            f"return {function_name(procedures[i])}(*arguments)"+LINE_END
        i += 1
    out_string += INDENT+f"else:"+LINE_END + \
        INDENT+INDENT + 'return "Invalid"'+LINE_END+LINE_END
    return out_string


def start():
    remote_procedures = json_loader('contract.json')['remote_procedures']
    f = open(FILE_NAME, "w")
    f.write(import_generator())
    f.write(config_generator())
    f.write(caller_builder(remote_procedures))
    f.write(rpc_builder())
    f.write(app_start_builder())
    """for procedure in remote_procedures:
        function_string = function_builder(procedure)
        f.write(function_string)"""
    f.close()


start()
