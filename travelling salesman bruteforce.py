def lex_suc(perm):
    #creating a copy
    res = bitlist[:]
    
    n = len(perm)
    
    for i in range(n-2, -1, -1):
        if perm[i] < perm[i+1]:
            break
    
    
    for j in range(n-1, i, -1):
        if perm[j] > perm[i]:
            break
    
    res[i], res[j] = res[j], res[i]
    
    return res[:i+1] + reversed(res[i+1:])
    
def permutations(a, b):
    
    first = list(range(a, b))
    last = list(reversed(first))
    res = [first]
    
    while res[-1] != last:
        
        res += [lex_suc_perm(res[-1])]
    
    return res
    

def travelling_salesman_bruteforce(dists):
    
    #cost function
    def cost(tour):
        res = 0
        for i in range(-1, len(tour)-1):
            res += dists[tour[i]][tour[i+1]]
        return res 
    

    #generate all possible solutions
    
    all_paths = permutations(1, len(dists)):
        
    #find maximum or minimum
    
    min_dist = [0] + all_paths[0]
    
    for tour in paths:
        if cost([0]+tour) < cost(min_dist):
            min_dist = [0] + tour
    
    return min_dist






    
   

    

