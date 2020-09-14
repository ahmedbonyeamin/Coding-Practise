def power(x, n):
    
    if n == 0:
        return 1
    
    else: 
        value = power(x, n//2)
        
        if n%2 == 0:
            value = value*value
        
        else:
            value = value*value*x
        
        return value
    

def power(x, n):
    
    stack = []
    
    while n > 0:
        stack.append(n)
        n = n//2
    
    res = 1
    
    while len(stack)>0:
        n = stack.pop()
    
    if n%2 == 0:
        res = res * res
        
    else:
        res = res * res * x
    
    return res


    
    
    