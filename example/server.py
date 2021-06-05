import sys
import socket

HOST, PORT = '127.0.0.1', 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

headers = """\
HTTP/1.1 200 OK
Server: Batman/2.1.1
Content-Type: text/html
"""

def generate_resp_header():
    return headers


def recvall(sock):
    BUFF_SIZE = 1024
    data = bytearray()
    while True:
        packet = sock.recv(BUFF_SIZE)
        if not packet or len(packet) < BUFF_SIZE:  # Important!!
            break
        data.extend(packet)
    return data


def request_handler(sock):
    datalist = []
    while True:
        conn, addr = sock.accept()

        request = recvall(conn)

        print(request)
        header_txt = generate_resp_header()
        body = 'Hello, World'
        resp_txt = '{}\r\n{}'.format(header_txt, body)
        conn.sendall(resp_txt.encode())

        conn.close()

try:
    sock.bind((HOST, PORT))
    sock.listen()
    print('listening http://{}:{}\n'.format(HOST, PORT))

    request_handler(sock)
except socket.error as e:
    sock.close()
    sys.exit(0)
except KeyboardInterrupt:
    sys.exit(0)
