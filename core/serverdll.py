from helper.CRC import *
from core.clientdll import CRC_KEY
from helper.strtobits import bitstostr

def serverdll(bits):
    packets = []
    bitstream = ""
    packets = bitsTopacketsServer(bits)
    for pack in packets:
        rem = mod2(pack,CRC_KEY)
        if rem == "000":
            bitstream += pack[0:len(pack)-3]
    
    org_msg = bitstostr(bitstream)
    return org_msg
    # for i in range(0,len(bitstream),8):
    #     a = ""
    #     a += bitstream[i:i+8]
    #     b = int(a,2)
    #     org_msg += chr(b)
    # return org_msg


def bitsTopacketsServer(msg):
    pack = []
    for i in range(0,len(msg),35):
        a = ""
        if i+32 < len(msg):
            a += msg[i:i+35]
        else:
            a += msg[i:len(msg)]
        pack.append(a)
    return pack