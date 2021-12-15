import socket

clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clnt.connect(('localhost', 1002))

file = open('foto.jpeg','rb')
image_data = file.read(2048)

while image_data:
    clnt.send(image_data)
    image_data = file.read(2048)
    
file.close()
clnt.close()