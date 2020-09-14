def empty_graph(n):
    graph = []
    for i in range(n):
        row = []
        for j in range(n):
            row += [0]
        
        graph.append(row)
    return graph

print(empty_graph(4))

def empty_graph1(n):
    return [n*[0] for i in range(n)]


print(empty_graph1(4))            