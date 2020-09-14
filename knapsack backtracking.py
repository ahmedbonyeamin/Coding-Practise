def solutions(completed, options, part=[]):


    if completed(part):
        return [part]
    
    else:

        res = []

        for o in options(part):
            augmented = part+[o]
            res += solution(completed, options, augmented)
        
        return res
    

def knapsack(values, weights, capacity):
    
    def weight(part):
        res = 0
        for i in range(len(part)):
            if part[i] == 1:
                res += weights[i]
        return res
    
    def value(part):
        res = 0
        for i in range(len(part)):
            if part[i] == 1:
                res += value[i]
        return res
    
    def completed(part):
        return len(part) == len(values)
    
    def options(part):
        if weight(part) + weights[len(part)] <= capacity:
            return [0, 1]
        else:
            return [0]
    
    sols = solutions(completed, options)
    
    return max(sols, key=value)
    
        
        

