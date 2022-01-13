from socket import (
    socket,
    AF_INET,
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)

#############################
# Variables
#############################
HOST, PORT = "127.0.0.1", 8080
request = f"GET / HTTP/1.1\r\nHost: {HOST}:{PORT}\r\n\r\n".encode()
response = ""
#############################

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.connect((HOST, PORT))
    # sending request
    sock.sendall(request)
    # receiving response
    while True:
        recv = sock.recv(1024)
        if recv == b'':
            break
        response += recv.decode()
    print(response)
