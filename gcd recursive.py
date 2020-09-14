def euclid_recursive(a, b):
    if b == 0:
        return a 
    
    else:
        return euclid_recursive(b, a%b)