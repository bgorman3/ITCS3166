import socket
import os

ServerPort = 12001

try:
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print (f'unable to establish a socket connection {err}\n')

try: 
    ServerSocket.bind(('localhost',ServerPort))
except socket.error as err:
    print (f'Unable to bind to the server {err}\n')

ServerSocket.listen(1)

print ('The server is ready to recieve your data \n')

while True:
    ConnectionSocket, Address = ServerSocket.accept()
    ClientMessage= ConnectionSocket.recv(1024)
    CapitalMessage = str(ClientMessage.decode()).upper()
    print (f'recived data is {ClientMessage.decode()}')
    print (f'data after capitalization {CapitalMessage}')
    ConnectionSocket.send(CapitalMessage.encode())
    ConnectionSocket.close()
    exit()