import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    try:
        a = input("Enter the sequence")
        client_socket.sendto(a.encode(),('localhost',12000))
        data,addr  = client_socket.recvfrom(1024)
        if data.decode() == 'Good':
            print("Well done")

        else:
            print("Failed")
            break
    finally:
        print("Done")