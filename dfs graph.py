"""Depth first search"""
def neighbours(v, g):
    return [j for j in range(len(g[v])) if g[v][j] == 1]


def dfs(graph, s):
    visited = []
    boundary = [s]
    
    while len(boundary) > 0:
        v = boundary.pop()
        #add to last, Access boundary by the last element = stack 
        visited += [v]
        
        for w in neighbours(v, graph):
            
            if w not in visited and w not in boundary:
                boundary.append(w)
            
    return visited

def dfs_traversal(graph, s, goals=[]):

    visited = []
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop()
        visited += [v]
        if v in goals:
            break
        for w in neighbours(v, graph):
            if w not in visited and w not in boundary:
                boundary.append(w)
    return visited


"""DFS PATH"""
def get_path(parent_list, s, e):
    reversed_path = [e]
    
    while reversed_path[-1] != s:
        v = reversed_path[-1]
        reversed_path.append(parent_list[v])
    
    path = reversed_path[::-1]
    
    return path

def dfs_path(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, dfs_path(g, 0, [9, 39]))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---004---005---006---007---008---009   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   010   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   011---012   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    visited = []
    boundary = [s]
    #############################
    parents = [None] * len(graph)
    #############################
    while len(boundary) > 0:
        v = boundary.pop()
        visited += [v]
        if v in goals:
            break
        for w in neighbours(v, graph):
            if w not in visited and w not in boundary:
                boundary.append(w)
                ###############
                parents[w] = v
                ###############
    
    e = visited[-1]
    shortest_path = get_path(parents, s, e)
                
    return shortest_path

