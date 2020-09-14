def bin(x):
    if x < 0:
        a = abs(x)
    else:
        a = x
    res = ''
    b = 1
    while b > 0:
        b = a // 2
        r = a % 2
        a = b
        res += str(r)
    res += 'b0'
    if x < 0:
        res += '-'
    binary = res[::-1]
    return binary