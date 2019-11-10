from helper.CRC import encode
from helper.bitsTopackets import bitsTopackets
from helper.err_gen import err_gen
from helper.framing import enFrame

PACKET_SIZE = 32
CRC_KEY = "1001"
FRAME_KEY = "01111110"

def clientdll(msg):
    packets = []
    encoded_packets = []
    packets = bitsTopackets(msg,PACKET_SIZE)
    for pack in packets:
        pack = encode(pack,CRC_KEY)
        # pack = err_gen(pack)
        pack = enFrame(pack,FRAME_KEY)
        encoded_packets.append(pack)

    return ''.join(encoded_packets)