import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12004
client_socket.connect(('localhost', port))

try:
    while True:
        msg = input("Enter a phrase")
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode('utf8')
        print("From server : ",data)
        if data=="exit":
            break
        else:
            continue
finally:
    print("Connection closed")
    client_socket.close()
