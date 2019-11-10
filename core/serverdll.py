from helper.CRC import *
from helper.framing import deFrame
from settings import CRC_KEY,FRAME_KEY


def serverdll(bits):
    bitstream = ""
    flag = 0

    # Removing the flags and extra bits
    packets = deFrame(bits,FRAME_KEY)
    
    # Error Detection using CRC
    for pack in packets:
        rem = mod2(pack,CRC_KEY)
        if rem == '0'*(len(CRC_KEY)-1):
            bitstream += pack[0:len(pack)-(len(CRC_KEY)-1)]
        else:
            org_msg = "Error found in a packet, please send the message again."
            flag = 1
            break
    if flag == 0:
        org_msg = bitstream

    return flag,org_msg