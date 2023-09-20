from socket import socket, AF_INET, SOCK_STREAM
server_name = 'localhost'
server_port = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
try:
    sentence = input('Input lowercase sentence:')
    client_socket.send(sentence.encode())
    modified_sentence = client_socket.recv(1024)
    print('From Server:', modified_sentence.decode())
finally:
    client_socket.close()
