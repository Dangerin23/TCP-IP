import socket
from main import run_server

s = socket.socket()
print("Socket successfully created")

port = 8011
s.bind(('',port))
print("socket binded to port no : ",port)
s.listen(5)

c,addr = s.accept()
print("Connected to client : ",addr)

data = c.recv(1024)
dat = data.decode()
flag,msg = run_server(data)
print(msg)
if flag==0:
    response = "Ok, Message received properly."
    res = response.encode()
    c.sendall(res)
else:
    response = "Error occured in Transmission."
    res = response.encode()
    c.sendall(res)
c.close()