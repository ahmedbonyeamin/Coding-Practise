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

def choose(length, n):

#check whether the parial solution is complete    
    def completed(part):
        return len(part) == len(length)
        
    
#find valid options for augmenting to the partial solution
    def options(part):
        if 1 + sum(part) <= n:
            return [0,1]
        else:
            return [0]         
    
    
    return solutions(completed, options)

print(choose([1,2,3], 2))


        

