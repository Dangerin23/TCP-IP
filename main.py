from core.clientdll import *
from core.serverdll import *
from core.clientpl import *
from core.serverpl import *
from helper.strtobits import *

def main():
    print("Enter message : ")
    s = input()
    s = strtobits(s)
    s = clientdll(s)
    s = serverdll(s)
    print(s)

if __name__ == "__main__":
    main()