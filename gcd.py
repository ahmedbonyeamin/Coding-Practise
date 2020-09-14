def gcd_brute_force(m, n):
    x = min(m, n)
    while not(m % x == 0 and n%x == 0):
        x = x-1
    return x

def gcd_euclid(m, n):
    while n != 0:
        r = m%n
        m, n = n, r
    return m


def euclid_recursive(a, b):
    if b == 0:
        return a 
    
    else:
        return euclid_recursive(b, a%b)
    

def euclid(a, b):
    
    #PRC:a, b == a0, b0 
    
    while b!= 0:
        #I: gcd(a,b) = gcd(a0, b0)
        
        a, b = b, a%b
        #I': gcd(a, b) = gcd(a0, b0)
        #EXC: b = 0
        #POC: a = gcd(a, b) = gcd(a0, b0)
        
    return a

