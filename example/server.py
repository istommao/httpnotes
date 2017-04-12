import sys
import socket

HOST, PORT = '127.0.0.1', 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def generate_resp_header():
    headers_lst = [
        'HTTP/1.1 200 OK',
        'Server: Batman/2.1.1',
        'Content-Type: text/html'
    ]

    combination_txt = '\n'.join(headers_lst)
    return combination_txt


def request_handler(sock):
    while 1:
        conn, addr = sock.accept()
        request = conn.recv(1024)
        print(request.decode())

        header_txt = generate_resp_header()
        body = 'Hello, World\n'
        resp_txt = '{}\n\n{}'.format(header_txt, body)
        conn.sendall(resp_txt.encode())

        conn.close()


try:
    sock.bind((HOST, PORT))
    sock.listen()
    print('listening http://{}:{}\n'.format(HOST, PORT))
except socket.error as e:
    sock.close()
    sys.exit(0)
else:
    request_handler(sock)
