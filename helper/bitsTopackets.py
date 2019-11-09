def bitsTopackets(msg,pack_size):
    pack = []
    for i in range(0,len(msg),pack_size):
        a = ""
        if i+pack_size < len(msg):
            a += msg[i:i+pack_size]
        else:
            a += msg[i:len(msg)]
        pack.append(a)
    return pack