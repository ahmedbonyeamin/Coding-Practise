def euclid_recursive(a, b):
    if b == 0:
        return a 
    
    else:
        return euclid_recursive(b, a%b)
    
def lcm(x, y):
    return (x*y)/euclid_recursive(x, y)

print(lcm(2, 3))    
    
