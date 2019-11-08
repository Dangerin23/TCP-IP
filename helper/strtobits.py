def strtobits(msg):
    bits = ""
    for i in range(0,len(msg)):
        bits += '{0:b}'.format(ord(msg[i]))
        while len(bits)<=8:
            bits = "0" + bits
    return bits
