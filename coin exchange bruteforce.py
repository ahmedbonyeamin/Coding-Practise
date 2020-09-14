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

def brute_force_coin_exchange(amount, denominations):
    """
    Input: The target amount of you want to reach and a list of 
           coins (i.e. denominations) that you have an infinite amount of.
    Output: A list of integers where each index represents the number of 
            coins the denominations list.

    >>> brute_force_coin_exchange(15, [10, 7, 6, 1])
    [0, 2, 0, 1]
    """    
    last = [amount//d for d in denominations]

    def no_of_coins(option):
        return sum(option)

    def is_equal_amount(option):
        weighted_option = [option[i]*denominations[i] for i in range(len(option))]
        value = sum(weighted_option)
        return value == amount
    #Generate all possible solution candidates
    possible_solutions = bounded_lists(last)

    #Filter for feasible solutions
    feasible_solutions = filter(is_equal_amount, possible_solutions)

    #find maximum or minimum
    return min(feasible_solutions, key=no_of_coins)

print(brute_force_coin_exchange(56, [20, 10, 5, 1]))


