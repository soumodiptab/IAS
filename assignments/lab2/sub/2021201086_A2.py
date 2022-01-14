import socket
import ssl
# Configuration -----------------------------
TARGET_PORT = 80
SSL_PORT = 443
BUFFER_SIZE = 4096
FORMAT = 'utf-8'
# --------------------------------------------


def secure_handler(url):
    """secure_handler Handles ssl based http connection requests

    Args:
        url (string): Host/Domain of the 

    Returns:
        string: Returns the html page
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_socket = ssl.wrap_socket(client, keyfile=None, certfile=None,
                                    server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
    secure_socket.connect((url, SSL_PORT))
    request = f"GET / HTTP/1.1\r\nHost: {url}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8\
        \r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0\
        \r\nConnection: Close\r\n\r\n"
    secure_socket.send(request.encode())
    response = response_handler(secure_socket)
    status_code = response.split('\r\n')[0].split(' ')[1]
    list_resp = response.split('\r\n\r\n')
    list_resp.pop(0)
    html_page = ''.join(list_resp)
    secure_socket.close()
    return html_page


def response_handler(conn):
    """response_handler Handles Http responses in buffered mode and returns the response

    Args:
        conn (socket): 

    Returns:
        string: The response after decoding
    """
    #response = client.recv(BUFFER_SIZE).decode()
    buffer = conn.recv(BUFFER_SIZE)
    response = buffer
    while (len(buffer) > 0):
        buffer = conn.recv(BUFFER_SIZE)
        response += buffer
    response = response.decode()
    return response


def start_browser():
    """start_browser Starts the command line browser
    """
    while True:
        print("------------------------------------------------------------------------------------------")
        print(' CMD BROWSER | Enter URL')
        print("------------------------------------------------------------------------------------------")
        url = input()
        TARGET_HOST = str(url)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((TARGET_HOST, TARGET_PORT))
        request = f"GET / HTTP/1.1\r\nHost: {TARGET_HOST}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8\
            \r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0\
            \r\nConnection: Close\r\n\r\n"
        client.send(request.encode())
        response = response_handler(client)
        status_code = response.split('\r\n')[0].split(' ')[1]
        list_resp = response.split('\r\n\r\n')
        list_resp.pop(0)
        client.close()
        html_page = ''.join(list_resp)
        if not status_code == '200':
            html_page = secure_handler(TARGET_HOST)
        print(html_page)


start_browser()
