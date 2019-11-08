from helper.CRC import *
CRC_KEY = "1001"

def clientdll(msg):
    packets = []
    encoded_packets = []
    packets = bitsTopackets(msg)
    for pack in packets:
        pack = encode(pack,CRC_KEY)
        encoded_packets.append(pack)
    res = ""
    for pack in encoded_packets:
        res += pack
    return res
    

def bitsTopackets(msg):
    pack = []
    for i in range(0,len(msg),32):
        a = ""
        if i+32 < len(msg):
            a += msg[i:i+32]
        else:
            a += msg[i:len(msg)]
        pack.append(a)
    return pack