import sys
sys.path.append('../')  
from helper.mod2 import mod2

def encoding(data,key):
    len_key = len(key)

    appended_data = data + '0'*(len_key-1)
    rem = mod2(appended_data,key)

    encoded = data + rem
    return rem