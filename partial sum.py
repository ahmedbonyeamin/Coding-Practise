def partial_sum(start, end, step):
    if end > 0:
        stop = end + 1
    else:
        stop = end - 1
    res = 0
    for i in range(start, stop, step):
        res = res + i
    return res