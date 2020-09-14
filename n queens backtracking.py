def is_attacked(r, c, partial):
    
    for i in range(len(partial)):
        if r in partial or abs(i-c) == abs(partial[i]-r):
            return True 
        
    return False

def options(partial, n):
    res = []
    col = len(partial)
    
    for row in range(n):
        if not is_attacked(row, col, partial):
            res += [row]
    return res

def queens(n, part=[]):
    
    if len(part) == n:
        return [part]
      
    else:
        res = []
        for o in options(part, n):
            res += queens(n, part+[o])
    
    
    return res

