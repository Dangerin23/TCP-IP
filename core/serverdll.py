from helper.CRC import *
from helper.bitsTopackets import *
from core.clientdll import CRC_KEY,PACKET_SIZE,FRAME_KEY
from helper.strtobits import bitstostr
from helper.framing import deFrame

def serverdll(bits):
    bitstream = ""
    flag = 0
    packets = deFrame(bits,FRAME_KEY)
    for pack in packets:
        rem = mod2(pack,CRC_KEY)
        if rem == '0'*(len(CRC_KEY)-1):
            bitstream += pack[0:len(pack)-(len(CRC_KEY)-1)]
        else:
            org_msg = "Error found in a packet, please send the message again."
            flag = 1
            break
    if flag == 0:
        org_msg = bitstostr(bitstream)

    return org_msg