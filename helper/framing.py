def enFrame(data,flag):
    key = flag[0:(len(flag)-1)]
    data = data.replace(key,key+'1')
    data = flag + data + flag
    return data

def deFrame(data,flag):
    data = data[len(flag):-len(flag)]
    frames = list(data.split(flag+flag))
    return frames

def RemBit(data,flag):
    key = flag[0:(len(flag)-1)]
    data = data.replace(key+'1',key)
    return data



