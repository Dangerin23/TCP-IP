from core.clientdll import *
from core.serverdll import *
from core.clientpl import *
from core.serverpl import *
from helper.strtobits import *

def main():
    print("Enter message : ")
    msg = input()
    bits = strtobits(msg)
    frames = clientdll(bits)
    signal = clientpl(frames)
    bits = serverpl(signal)
    flag,stream = serverdll(bits)
    if flag==0:
        rev_msg = bitstostr(stream)
        print(rev_msg)
    else:
        print(stream)

if __name__ == "__main__":
    main()