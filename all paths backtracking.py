def all_paths(M, u, v):
    """
    Input: Graph 'M' as adjacency matrix, and vertexes 'u' and 'v'
    Output: List of vertices in lexicographical order that finds 
            all paths from 'u' to 'v'.
    
    For Example:
    >>> M = [ [0, 1, 1, 0],
    ...       [1, 0, 1, 1],
    ...       [1, 1, 0, 0],
    ...       [0, 1, 0, 0]]
    >>> all_paths(M, 0, 1)
    [[0, 1], [0, 2, 1]]
    >>> all_paths(M, 1, 0)
    [[1, 0], [1, 2, 0]]
    >>> all_paths(M, 0, 3)
    [[0, 1, 3], [0, 2, 1, 3]]
    >>> all_paths(M, 2, 3)
    [[2, 0, 1, 3], [2, 1, 3]]
    """
    def completed(part):
        return part[-1] == v
    
    def neighbours(v, graph):
        return [j for j in range(len(graph)) if graph[v][j]]

    def options(part):
        vertex = part[-1]
        option = [i for i in neighbours(vertex, M) if not i in part]
        return option
    
    starting_partial = [u]
    def solutions(completed, options, part=[]):

        if completed(part):
            return [part]
        
        else:

            res = []

            for o in options(part):
                augmented = part+[o]
                res += solutions(completed, options, augmented)
            
            return res
    
    
    return solutions(completed, options, starting_partial)