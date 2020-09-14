def lex_suc(bitlist):
    #creating a copy
    res = bitlist[:]
    
    i = len(bitlist) - 1
    
    while res[i] == 0:
        res[i] = 1
        i = i-1
    res[i] = 0
    return res
    
def bitlist(n):
    
    first = [0]*n
    last = [1]*n
    res = [first]
    
    while res[-1] != last:
        
        res += [lex_suc(res[-1])]
    
    return res

print(bitlist(3))