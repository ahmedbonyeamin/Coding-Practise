def greedy_exchange(amount, denominations):
    """
    >>> greedy_exchange(56, [20, 10, 5, 1])
    [2, 1, 1, 1]
    >>> greedy_exchange(350, [100, 50, 10, 5, 2, 1])
    [3, 1, 0, 0, 0, 0]
    >>> greedy_exchange(12, [9, 6, 5, 1])
    [1, 0, 0, 3]
    """
    total = 0
    res = []
    
    for i in range(len(denominations)):
        c = (amount - total)// denominations[i]
        res.append(c)
        total += c*denominations[i]
        
    
    return res

