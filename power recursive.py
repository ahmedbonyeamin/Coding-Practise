def power_recursive(x, n):
    
    if n <= 1:
        return x
    
    else:
        return (x * power_recursive(x, n-1))
    

print(power_recursive(2, 4))


    