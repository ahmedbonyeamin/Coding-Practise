def lex_suc_bounded_upper(lst, upper):
    
    res = lst[:]
    i = len(res) - 1

    while res[i] == upper[i]:
    
        res[i] = 0
        
        i = i-1
    
    res[i] = res[i] +  1
    
    return res

def bounded_lists(upper_bounds):
    """
    Input: List of positive integers of length 'n'
    Output: List of lists where i, lst[i] <= upper_bound[i]

    >>> bounded_lists([1, 1, 2])
    [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]
    """
    n = len(upper_bounds)
    first = n*[0]
    res = [first]
    
    while res[-1] != upper_bounds:

        res += [lex_suc_bounded_upper(res[-1], upper_bounds)]
    
    return res
