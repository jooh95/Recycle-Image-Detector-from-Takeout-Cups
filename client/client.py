import socket
import numpy

FILENAME = "C:\Users\caucse\Desktop\image.png"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('165.194.17.28', 12345))

print("client connected...")

file = open(FILENAME, 'rb')

try:
    data = file.read(1024)
    while data:
        sock.send(data)
        data = file.read(1024)
except Exception as e:
    print(e)

