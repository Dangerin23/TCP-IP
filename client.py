import socket
from main import run_client

def main():
    host = "127.0.0.1"
    port = 8011

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))

    while True:
        print("Enter your message")
        message = input()
        signal = run_client(message)
        s.send(signal.encode())

        data = s.recv(1024)
        dat = data.decode()

        print("From Server: ",dat)
        ans = input("\nDo you want to send again? (y/n) : ")
        if ans=='y':
            continue
        else:
            break
    s.close()

if __name__ == "__main__":
    main()