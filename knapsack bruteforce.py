def lex_suc(bitlist):
    #creating a copy
    res = bitlist[:]
    
    i = len(bitlist) - 1
    
    while res[i] == 1:
        res[i] = 0
        i = i-1
    res[i] = 1
    return res
    
def bitlists(n):
    
    first = [0]*n
    last = [1]*n
    res = [first]
    
    while res[-1] != last:
        
        res += [lex_suc(res[-1])]
    
    return res
    

def knapsack_bruteforce(weights, values, capacity):
    
    def is_feasible(subset):
        weight = 0
        for i in range(len(subset)):
            if subset[i] == 1:
                weight += weights[i]
        return weight <= capacity
    
    def value(subset):
        value = 0
        for i in range(len(subset)):
            if subset[i] == 1:
                value += values[i]
        return value
    
    #generate all possible solutions
    all_subsets = bitlists(len(values))
   
    #Filter for feasible solutions
    feasible_subsets = filter(is_feasible, all_subsets)
    
    #find maximum or minimum
    return max(feasible_subsets, key=value)




    
   

    

