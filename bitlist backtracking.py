#General Backtracking 

#represent the partial solution



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

def bitlists(length):

#check whether the parial solution is complete    
    def completed(part):
        return len(part) == length
    
#find valid options for augmenting to the partial solution
    def options(part):
        return [0,1]        
    
    
    return solutions(completed, options)

print(bitlists(3))


        


