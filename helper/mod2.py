def XOR(x,y):
    ans = []
    for i in range(1, len(y)): 
        if x[i] == y[i]: 
            ans.append('0') 
        else: 
            ans.append('1') 
  
    return ''.join(ans) 

def mod2(dividend,divisor):
    ind = len(divisor)

    temp = dividend[0:ind]

    while(ind<len(dividend)):

        if temp[0] == '1':
            temp = XOR(divisor,temp) + dividend[ind]

        else :
            temp = XOR('0'*ind,temp) + dividend[ind]
        
        ind+=1

    if temp[0] =='1':
        temp = XOR(divisor,temp)

    else:
        temp = XOR('0'*ind,temp)

    check = temp
    return check