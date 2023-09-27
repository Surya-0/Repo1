from socket import socket, AF_INET, SOCK_DGRAM
server_name = 'localhost'
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
try:
    message = int(input("Input lowercase sentence:"))
    client_socket.sendto(message.encode(), (server_name, server_port))
    modified_message, server_address = client_socket.recvfrom(2048)
    print(modified_message.decode())
finally:
    client_socket.close()
