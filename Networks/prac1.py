from socket import *
import socket
import sys
try:
    sock = socket.socket(family=AF_INET,
                      type=SOCK_STREAM)  # AF_INET family for our sockets and SOCK_STREAM is for TCP sockets
except socket.error as err:
    print("socket not created")
    sys.exit(1)
print("Socket created")

target_host = 'localhost'
target_port = 12000
try:
    sock.connect((target_host, target_port))

except socket.error as err:
    print("Failed to connect to %s: %s" % (target_host, target_port))
    print("Read error: %s" % err)
    sys.exit(1)
