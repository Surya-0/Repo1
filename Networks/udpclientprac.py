import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input("Enter message")
client_socket.sendto(msg.encode("utf-8"), ('localhost',12000))
data,addr = client_socket.recvfrom(2048)
print("Server says ", data.decode())
client_socket.close()