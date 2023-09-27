import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost',12000))
print("Server is ready to receive")
while True:
    data,addr = server_socket.recvfrom(1024)
    print("The data received is ",data.decode('utf-8')," from address ",addr)
    l = data.decode('utf-8').split(" ")
    print(l)
    for i in range(len(l)):
        l[i] = int(l[i])
    if (l[1]-l[2] == l[0]):
        ans = "Good"
    else:
        ans = "Bad"
    server_socket.sendto(ans.encode(),addr)
