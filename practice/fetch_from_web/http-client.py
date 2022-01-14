import socket
target_host = "www.google.com"

target_port = 80  # create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
client.send(request.encode())

# receive some data
BUFF_SIZE = 4096  # 4 KiB
data = b''
while True:
    part = client.recv(BUFF_SIZE)
    data += part
    if len(part) < BUFF_SIZE:
        # either 0 or end of data
        break
#response = client.recv(8196)
print("------------------------------------------------------------------------------------------")
response_dec = data.decode()
http_response_len = len(response_dec)
print(http_response_len)
print(response_dec)
