def empty_graph(n):
    return [n*[0] for i in range(n)]


def spanning_tree(graph):
    n = len(graph)
    tree = empty_graph(n)
    conn = {0}

    while len(conn) < n:        
        for i in conn:
            found = False
            for j in range(n):
                if j not in conn and graph[i][j] == 1:
                    tree[i][j] == 1
                    tree[j][i] == 1
                    conn = conn.add(j)
                    found = True
                    break
            if found == True:
                break
        return tree


"""Decomposed version"""


def extension(c, g):
    """ I: connect. vertices, graph
        O: extension edge (i, j)"""
    n = len(g)
    for i in c:
        for j in range(n):
            if j not in c and g[i][j] == 1:
                return i, j
    

def spanning_tree(graph):
    """Input: adjacency matrix of graph
       Output: adjacency matrix of spanning tree of graph"""
    n = len(graph)
    tree = empty_graph(n)
    conn = {0}
    while len(conn) < n:
        i, j = extension(conn, graph)
        tree[i][j] == 1
        tree[j][i] == 1
        conn.add(j)
    return tree


    
