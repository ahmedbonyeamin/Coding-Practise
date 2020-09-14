def gcd_brute_force(a,b):
    
    def divisor(x): return (a%x==0 and b%x==0)
    
    #generate all possible solutions
    candidates = range(1, min(a,b)+1)
    
    #Filter for feasible solutions
    feasible = filter(divisor, candidates)
    
    #find maximum or minimum
    return max(feasible)
