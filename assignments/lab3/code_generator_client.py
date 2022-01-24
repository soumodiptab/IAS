import json
import sys
# --Configuration-----------------
FILE_NAME = 'rpc_client.py'
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


imports = ["socket"]
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
    return out_string


def config_generator():
    out_string = ""
    for c in config.keys():
        out_string = out_string+f"{c} = {config[c]}"+LINE_END
    return out_string


def rpc_builder():
    outstring = LINE_END+"def rpc_connector(func_name, param_list):"+LINE_END +\
        INDENT + "client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)"+LINE_END +\
        INDENT + "client.connect(ADDRESS)"+LINE_END +\
        INDENT + "func_dict_str = str({func_name: param_list}).encode()"+LINE_END +\
        INDENT + "client.send(func_dict_str)"+LINE_END +\
        INDENT + "func_ret = client.recv(MAX_sIZE).decode()"+LINE_END +\
        INDENT + "return func_ret"+LINE_END+LINE_END
    return outstring


def function_builder(procedure):
    function_name = procedure["procedure_name"]
    parameter_list = procedure["parameters"]
    return_type = procedure["return_type"]
    if return_type == "string":
        return_type = "str"
    out_string = LINE_END+f"def {function_name}("
    for param in parameter_list:
        param_type = param["data_type"]
        if param_type == "string":
            param_type = "str"
        out_string = out_string+param["parameter_name"]+":"+param_type+","
    if len(parameter_list) > 0:
        out_string = out_string[:-1]
    out_string += "):"+LINE_END
    out_string = out_string+INDENT + \
        f"return {return_type}(rpc_connector('{function_name}',["
    if len(parameter_list) == 0:
        return out_string+"]))"+LINE_END+LINE_END
    for param in parameter_list:
        out_string = out_string+param["parameter_name"]+","
    out_string = out_string[:-1]+"]))"+LINE_END+LINE_END
    return out_string


def start(file_name):
    remote_procedures = json_loader(file_name)['remote_procedures']
    f = open(FILE_NAME, "w")
    f.write(import_generator())
    f.write(config_generator())
    f.write(rpc_builder())
    for procedure in remote_procedures:
        function_string = function_builder(procedure)
        f.write(function_string)
    f.close()


if len(sys.argv) != 2:
    exit()
start(sys.argv[1])
