from socket import *
import threading

def handle_client(connectionSocket, addr):
    try:
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5) 
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()
