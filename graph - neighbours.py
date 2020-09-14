def neighbours(v, g):
    
    res= []
    
    for j in range(len(g[v])):
        
        if g[v][j] == 1:
            res.append(j)
            
    return res
            
def neighbours1(v, g):
    return [j for j in range(len(g[v])) if g[v][j] == 1]


            