lec_graph = [[2, 4, 5, 6, 7],
             [2, 3, 5, 6 ,7],
             [0, 1, 6, 7],
             [1, 4, 7],
             [0, 3, 6],
             [0, 1],
             [0, 1, 2, 4, 7],
             [0, 1, 2, 4, 7]]



def independent_set(adj_list, seq):
    for i in range(len(seq)-1):
        for j in range(i+1, len(seq)):
            if seq[j] in adj_list[seq[i]]:
                return False
    return True 


def greedy_indset(adj_list):
    
    def num_neighbours(i):
        return len(adj_list[i])
    
    
    vertices = sorted(range(len(adj_list)), key=num_neighbours)
    
    res = []
    for i in vertices:
        if independent_set(adj_list, [i] + res):
            res += [i]
        
    return res

x = greedy_indset(lec_graph)
print(independent_set(lec_graph, x))
print(len(x))



