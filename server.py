import socket
from _thread import *
import threading
from main import run_server

print_lock = threading.Lock()

def threadFunc(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('Bye')
            print_lock.release()
            break

        sig = data.decode()
        flag,msg = run_server(sig)
        print(msg)
        if flag==0:
            response = "Ok, message received."
            c.send(response.encode())
        else:
            response = "Error Occured in transmission."
            c.send(response.encode())
    c.close()

def main():
    host = ""
    port = 8011

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(5)
    print("Server is listening at port : ",port)

    while True:
        client,addr = s.accept()
        print_lock.acquire()
        print("Connected to ",addr[0],":",addr[1])

        start_new_thread(threadFunc,(client,))
    s.close()

if __name__ == "__main__":
    main()