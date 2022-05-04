import socket
import ssl
from urllib.parse import urlparse
# Configuration -----------------------------
HTTP_PORT = 80
SSL_PORT = 443
BUFFER_SIZE = 4096
FORMAT = 'utf-8'
# --------------------------------------------


def url_validator(url):
    p = urlparse(url)
    if not (p.hostname and p.scheme):
        return False
    return True


def ssl_wrapper(conn):
    secure_socket = ssl.wrap_socket(conn, keyfile=None, certfile=None, server_side=False,
                                    cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
    return secure_socket, SSL_PORT


def request_handler(conn, parsedurl):
    path = "/"
    if parsedurl.path:
        path = parsedurl.path
    request = f"GET {path} HTTP/1.1\r\nHost: {parsedurl.hostname}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8\
            \r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0\
            \r\nConnection: Close\r\n\r\n"
    conn.send(request.encode())


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
        TARGET_PORT = HTTP_PORT
        print("------------------------------------------------------------------------------------------")
        print(' CMD BROWSER | Enter URL | EX: https://www.iiit.ac.in')
        print("------------------------------------------------------------------------------------------")
        url = str(input())
        if url == 'exit':
            break
        if not url_validator(url):
            print('Incorrect url correct format: https://www.google.com')
            continue
        parsed_url = urlparse(url)
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if parsed_url.scheme == "https":
            conn, TARGET_PORT = ssl_wrapper(conn)
        try:
            conn.connect((parsed_url.hostname, TARGET_PORT))
        except:
            print('Incorrect url')
            continue
        request_handler(conn, parsed_url)
        response = response_handler(conn)
        status_code = response.split('\r\n')[0].split(' ')[1]
        list_resp = response.split('\r\n\r\n')
        list_resp.pop(0)
        conn.close()
        html_page = ''.join(list_resp)
        # if not status_code == '200':
        #     html_page = secure_handler(TARGET_HOST)
        print(html_page)


start_browser()
