import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect as client to a selected server
# on a specified port

HOST, PORT = '127.0.0.1', 3000
sock.connect((HOST, PORT))

# Protocol exchange - sends and receives
url = '/asdf'
request_header = '{} {} {}'.format('GET', url, 'HTTP/1.1')
request = request_header.encode()
sock.send(request)

try:
    while 1:
        resp = sock.recv(1024)
        if resp == ''.encode():
            break
        print(resp.decode())

except socket.error as error:
    sock.close()
    sys.exit(0)
