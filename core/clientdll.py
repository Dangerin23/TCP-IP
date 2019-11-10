from helper.CRC import encode
from helper.bitsTopackets import bitsTopackets
from helper.err_gen import err_gen
from helper.framing import enFrame
from settings import PACKET_SIZE,CRC_KEY,FRAME_KEY

def clientdll(msg):
    packets = []
    encoded_packets = []

    # Convert bits to 32 bit packets
    packets = bitsTopackets(msg,PACKET_SIZE)

    # Apply CRC and Encode the packet
    for pack in packets:
        pack = encode(pack,CRC_KEY)
        encoded_packets.append(pack)
    
    # Generate an Error
    text = ''.join(encoded_packets)
    text = err_gen(text)
    packets = bitsTopackets(text,PACKET_SIZE+(len(CRC_KEY)-1))
    
    # Generate frames by adding flags and bit stuffing
    frames = []
    for pack in packets:
        pack = enFrame(pack,FRAME_KEY)
        frames.append(pack)

    return frames