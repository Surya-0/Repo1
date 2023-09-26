import  socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost',12000))

print("Server is ready to receive")
data,addr = server_socket.recvfrom(2048)
print(data,addr)

message = data.decode().upper()
server_socket.sendto(message.encode('utf-8'),addr)

