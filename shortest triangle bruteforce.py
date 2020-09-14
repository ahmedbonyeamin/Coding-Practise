def ordered_triples(n):
    res = []
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(i+2, n):
                res += [(i, j, k)]
                
    return res 

def shortest_triangle_bruteforce(graph):
    
    def is_cycle(triple):
        i, j, k = triple
        return graph[i][j] and graph[j][k] and graph[k][i]
    
    def weight(cycle):
        i, j, k = cycle
        return graph[i][j] + graph[j][k] + graph[k][i]
    
    #generate all possible solutions
    
    triples = ordered_triples(len(graph))
    
    
    #Filter for feasible solutions
    
    cycles = filter(is_cycle, triples)
   
    #find maximum or minimum
    
    return min(cycles, key = weight)


    

