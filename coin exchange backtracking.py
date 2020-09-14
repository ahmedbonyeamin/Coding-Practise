def solutions(completed, options, part=[]):    
    
#Base case    
    if completed(part):
        return [part]
    
    else:

        res = []

        for o in options(part):
            augmented = part+[o]
            res += solutions(completed, options, augmented)
        
        return res

def coin_change_backtracking(amount, denominations):

#check whether the parial solution is complete    
    def completed(part):
        return len(part) == len(denominations) and amount - total(part)== 0
    
    def total(part):
        return sum([part[i]*denominations[i] for i in range(len(part))])
    
#find valid options for augmenting to the partial solution
    def options(part):
        if len(part) == len(denominations):
            return []
        else:
            remaining = amount - total(part)
            max_coins = remaining // denominations[len(part)]
            return reversed(range(max_coins+1))
    
    sols = solutions(completed, options)         
    
    return min(sols, key=sum, default = None)

print(coin_change_backtracking(56, [20, 10, 5, 1]))
        

