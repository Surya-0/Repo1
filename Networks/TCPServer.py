from socket import *

serverPort = 12000
# AF_INET is the address family where the socket can communicate with the ipv4 addresses
serverSocket = socket(AF_INET, SOCK_STREAM)  # SOCK_STREAM indicates the socket is of TCP type
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
