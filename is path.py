def is_path(graph, path):
    for n in range(len(path)-1):
        i = path[n]
        j= path[n+1]
        if not(graph[i][j] == 1 and graph[j][i] == 1):
            return False
    return True 
