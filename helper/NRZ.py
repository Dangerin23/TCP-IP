def rev(a):
    if(a=='l'): return 'h'
    elif a=='h': return 'l'

def bitstoNRZ(bitstream):
    nrz = ""
    pre = bitstream[0]
    if(pre=='0'):
        nrz+='l'
    else:
        nrz+='h'
    l = len(bitstream)
    pre = 0
    curr = 1
    while curr<l :
        if bitstream[curr]=='0':
            nrz+=nrz[pre]
        else:
            nrz+=rev(nrz[pre])
        pre += 1
        curr += 1
    
    return nrz


def NRZtobits(nrz):
    bitstream=""
    if nrz[0] == 'h':
        bitstream += '1'
    else :
        bitstream = '0'
    
    pre = 0

    l = len(nrz)

    for i in range(1,l):
        if nrz[i] == nrz[pre]:
            bitstream += '0'
        else:
            bitstream += '1'
        
        pre+=1

    return bitstream

# temp = "1001"
# print(bitstoNRZ(temp))
# print(NRZtobits(bitstoNRZ(temp)))


