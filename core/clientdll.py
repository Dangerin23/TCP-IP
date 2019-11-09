from helper.CRC import *
from helper.bitsTopackets import bitsTopackets
from helper.err_gen import err_gen

PACKET_SIZE = 32
CRC_KEY = "1001"

def clientdll(msg):
    packets = []
    encoded_packets = []
    packets = bitsTopackets(msg,PACKET_SIZE)
    for pack in packets:
        pack = encode(pack,CRC_KEY)
        pack = err_gen(pack)
        encoded_packets.append(pack)

    return ''.join(encoded_packets)