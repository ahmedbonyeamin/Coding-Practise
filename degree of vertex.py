def degree(graph, vertex):
    count = 0
    for j in range(len(graph[vertex])):
        if graph[vertex][j] == 1:
            count += 1
            
    return count 


def shared_adjacent_vertices(graph, u, v):
    res = []
    for j in range(len(graph[u])):
        if (graph[u][j] == 1 and graph[v][j] == 1):
                     res.append(j)
    return res 


def adjacent(graph, u, v):
    return bool(graph[u][v])

def clique(graph, vertices):
    for i in range(len(vertices)-1):
        for j in range(i+1, len(vertices)):
            u, v= vertices[i], vertices[j]
            if graph[u][v] != 1:
                return False
    return True

empty_m = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

simple_m = [[0,1,1,1],
            [1,0,1,0],
            [1,1,0,0],
            [1,0,0,0]]

example_m = [[0,1,1,1,0],
             [1,0,0,0,0],
             [1,0,0,1,1],
             [1,0,1,0,1],
             [0,0,1,1,0]]

print(clique(empty_m,[0,1])),
print(clique(simple_m,[0,1,2]))
print(clique(example_m,[2,3,4]))


                     