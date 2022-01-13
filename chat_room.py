import socket

print("Press 1 for Server and 2 for Client<<<")
typ = input("Enter your choice: ")

if(typ == '1'):
    ServerSocket = socket.socket()

    ServerSocket.bind((socket.gethostname(),8080))
    ServerSocket.listen()
    print(">>>LISTENING<<<")
    clientSocket, addr = ServerSocket.accept()
    print ('>>>Client got connected<<<')
    while 1:
        message = clientSocket.recv(1024)
        message = message.decode('ascii')
        print('>>>Client: ',message)
        msg = input("Server: ")
        msg = "GET / HTTP/1.1\r\n" + msg + "\r\n"
        clientSocket.send(msg.encode('ascii'))
    clientSocket.close()          
    ServerSocket.close()
elif(typ == '2'):
    sock = socket.socket()
    sock.connect((socket.gethostname(),8080))
    print(">>>Connected<<<")
    while 1:
        msg = input("Client: ")
        msg = "GET / HTTP/1.1\r\n" + msg + "\r\n"
        sock.send(msg.encode())
        msg  = sock.recv(1024)
        msg = msg.decode('ascii')
        print("Server: ",msg)
    sock.close()
else:
    print(">>>Incorrect Choice<<<")