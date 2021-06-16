import sys
import socket

import traceback

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Connect as client to a selected server
# on a specified port

HOST, PORT = '127.0.0.1', 33333
sock.connect((HOST, PORT))

# Protocol exchange - sends and receives
url = '/'

body = """a=b&c=d""" * 1000

print(len(body.encode()))

datatpl = """\
{} {} {}
{}

{}
"""

request_data = datatpl.format('GET', url, 'HTTP/1.1',
    'Content-Type: application/x-www-form-urlencoded',
    body
)
# print(request_data)
sock.send(request_data.encode())

try:
    while True:
        resp = sock.recv(1024)
        if resp == ''.encode():
            break

        print(resp.decode())

        sock.close()
        break
except socket.error as error:
    traceback.print_exc()
    print(error)
    sock.close()
    sys.exit(0)
