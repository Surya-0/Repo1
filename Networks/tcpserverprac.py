from socket import *
import socket

server_socket = socket.socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost',12004)) # paramets are the server address and the port number
server_socket.listen(1)

print("server is ready to receive")
connection_socket,addr = server_socket.accept()
print("client connected from",addr)
while True:
    data = connection_socket.recv(1024).decode()
    print("received from client : %",data)
    capital_data = data.upper()
    try:
        connection_socket.send(capital_data.encode())
    except:
        print("Exiting due to unexpected exception")
    connection_socket.close()

