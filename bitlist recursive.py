def rbitlists(n):
    
    if n == 0:
        return [[]]
    
    else:
        smaller = rbitlists(n-1)
        return [lst for lst in smaller + [0]] + [lst for lst in smaller + [1]]
    

print(rbitlists(3))


