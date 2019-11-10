import random

def err_gen(bits):
    r = random.randint(1,50)
    if r == 50:
        ls = random.sample(range(len(bits)),3)
        for b in ls:
            bits = changeBit(bits,b)
    elif r >= 48:
        ls = random.sample(range(len(bits)),2)
        for b in ls:
            bits = changeBit(bits,b)
    elif r>=44:
        b = random.randint(0,len(bits))
        bits = changeBit(bits,b)

    # b = random.randint(0,len(bits))
    # bits = changeBit(bits,b)

    return bits

def changeBit(bits,i):
    new = list(bits)
    if new[i]=='0':
        new[i] = '1'
    else:
        new[i] = '0'
    return ''.join(new)