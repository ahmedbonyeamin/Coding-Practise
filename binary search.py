def binary_search(v, seq):
    
    a = 0
    b = len(seq) - 1
    c = (a+b) // 2
    
    while a <= b:
        
        if seq[c] == v:
            return c
        
        elif seq[c] > v:
            b = c - 1
        
        else:
            a = c + 1
    
    return None 