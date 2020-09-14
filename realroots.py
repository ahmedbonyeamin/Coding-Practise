def real_roots(a, b, c):
    discriminant = (b**2) - (4*a*c)
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [(-b)/2*a]
    else:
        root_1 = ((-b) + discriminant ** (1/2)) / 2*a
        root_2 = ((-b) - discriminant ** (1/2)) / 2*a
        return [root_1, root_2]

        

def rounding(n):
    remainder = n%10
    num = n - remainder
    if remainder < 5:
        return num
    elif remainder > 5:
        return num + 10
    else:
        if (num//10)%2 == 0:
            return num
        else:
            return num + 10
        
def decimal_rounding(n):
    remainder = n%1
    num = n - remainder
    if remainder < 0.5:
        return num
    elif remainder > 0.5:
        return num + 1
    else:
        if num%2 == 0:
            return num
        else:
            return num + 1

        
