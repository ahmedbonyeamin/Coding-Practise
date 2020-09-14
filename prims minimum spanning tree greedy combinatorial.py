import math

def empty_graph(n):
    return [n*[0] for i in range(n)]


def min_extension(c, g):
    
    min_weight = math.inf
    
    for i in c:
        for j in range(len(g)):
            if j not in c and 0 < g[i][j] < min_weight:
                v, w = i, j
                min_weight = g[i][j]
    
    return v, w

def minimum_spanning_tree(graph):
    tree = empty_graph(len(graph))
    con = [0]
    
    while len(con) < len(graph):
        i, j = min_extension(con, graph)
        tree[i][j], tree[j][i] = graph[i][j], graph[j][i]
        con += [j]
    return tree




        
        