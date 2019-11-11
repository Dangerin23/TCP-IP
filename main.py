from core.clientdll import clientdll
from core.serverdll import serverdll
from core.clientpl import clientpl
from core.serverpl import serverpl
from helper.strtobits import *

def run_client(msg):
    bits = strtobits(msg)
    frames = clientdll(bits)
    signal = clientpl(frames)

    return signal

def run_server(signal):
    bits = serverpl(signal)
    flag,stream = serverdll(bits)
    if flag==0:
        stream = bitstostr(stream)
    
    return flag,stream