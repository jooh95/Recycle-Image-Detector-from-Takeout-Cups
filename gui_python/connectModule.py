import socket

host = '13.125.234.52'   #amazon server address
PORT = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connectServer():
    sock.connect((host, PORT))
    
    
def getLoginResult(id, password):
    
    connectServer()
    
    sock.send(id.encode())
    #sock.send('/'.encode())
    #print("aaa" + str(nPassword.encode()))
    sock.send(str(password).encode())
    
    loginResult = sock.recv(1024).decode()
    
    sock.close()
    return loginResult

def insertDB(id, password, name, factory_region, factory_name):
    connectServer()
    
    sock.send(str(id).encode())
    sock.send(str(password).encode())
    sock.send(str(name).encode())
    sock.send(str(factory_region).encode())
    sock.send(str(factory_name).encode())
    
    sock.close()