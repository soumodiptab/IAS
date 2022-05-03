import socket
import threading
# Configuration
PORT1 = 5000
PORT2 = 5001
IP_ADDRESS = socket.gethostbyname((socket.gethostname()))
FORMAT = 'utf-8'
# Read from command line and write to socket
byeflag = False


def socket_writer(conn):
    global byeflag
    try:
        while True:
            msg = conn.recv(1024).decode(FORMAT)
            print(f"\n>> {msg}\n<<", end=" ")
            if msg == "bye":
                break
    except:
        print('Closing...')

# Read from socket and write to command line


def socket_reader(conn):
    global byeflag
    try:
        while True:
            msg = input('\n<<')
            conn.send(msg.encode(FORMAT))
            if msg == "bye":
                break
    except:
        print('Closing...')
# start prog and select first client - which will wait for the 2nd client to start


def start():
    choice = int(
        input('Press 1 for client1[waiting] and 2 for client 2[initial connector]\n'))
    if choice == 1:
        SOCKET = (IP_ADDRESS, PORT1)
        client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client1.bind(SOCKET)
        client1.listen()  # setting up listener
        conn, addr = client1.accept()
        print(f"Connected to {addr}")
        c1_reader = threading.Thread(target=socket_reader, args=(conn,))
        c1_writer = threading.Thread(target=socket_writer, args=(conn,))
        c1_reader.start()
        c1_writer.start()
        c1_reader.join()
        c1_writer.join()
        conn.close()
        client1.close()
    else:
        SOCKET = (IP_ADDRESS, PORT1)  # connect to waiting listener
        client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client2.connect(SOCKET)
        c2_reader = threading.Thread(target=socket_reader, args=(client2,))
        c2_writer = threading.Thread(target=socket_writer, args=(client2,))
        c2_reader.start()
        c2_writer.start()
        c2_reader.join()
        c2_writer.join()
        client2.close()


start()
