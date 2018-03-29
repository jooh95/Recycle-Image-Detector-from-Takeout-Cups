import socket

IP = "165.194.17.28"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(0)
client_socket, addr = server_socket.accept()

file = open("C:\Users\caucse\Desktop\image2.png", 'wb')
while(True):



    data = client_socket.recv(1024)
    try:
        while data:
            file.write(data)
            data = client_socket.recv(1024)
    except Exception as e:
        print(e)


    print(data)

