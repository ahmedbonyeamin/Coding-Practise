def lcm(a, b):
    m, n = a, b
    while n != 0:
        r = m%n
        m, n = n, r
    return (a*b)/m

print(lcm(7,6))


        