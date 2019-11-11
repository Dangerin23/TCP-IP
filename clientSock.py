import socket 
from main import run_client

s = socket.socket()
port = 8011
host = "127.0.0.1"

s.connect((host,port))

msg = input()
signal = run_client(msg)
sg = signal.encode()
s.sendall(sg)
out = s.recv(1024)
outp = out.decode()
print(outp)

s.close()