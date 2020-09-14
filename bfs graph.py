"""Breadth first search"""

def neighbours(v, g):
    return [j for j in range(len(g[v])) if g[v][j] == 1]

def bfs(graph, s):
    visited = []
    boundary = [s]
    
    while len(boundary) > 0:
        #O(n)
        v = boundary.pop(0)
        
        #add to last, Access boundary by the first element = qeue
        visited += [v]
        
        for w in neighbours(v, graph):
            
            if w not in visited and w not in boundary:
                boundary.append(w)
            
    return visited

"""Using deque"""
from collections import deque

def bfs(graph, s):
    visited = []
    boundary = deque([s])
    
    while len(boundary) > 0:
        
        #O(1)
        v = boundary.popleft()
        
        #add to last, Access boundary by the first element = qeue
        visited += [v]
        
        for w in neighbours(v, graph):
            
            if w not in visited and w not in boundary:
                boundary.append(w)
            
    return visited

def bfs_traversal(graph, s, goals=[]):
    visited = []
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop(0)
        visited += [v]
        if v in goals:
            break
        for w in neighbours(v, graph):
            if w not in visited and w not in boundary:
                boundary.append(w)
    return visited


"""BFS PATH AKA SHORTEST DISTANCES"""
import math
def bfs_distances(graph, s):
    dist = [math.inf] * len(graph)
    dist[s] = 0
    visited = []
    boundary = deque([s])
    
    while len(boundary) > 0:
        
        #O(1)
        v = boundary.popleft()
        
        #add to last, Access boundary by the first element = qeue
        visited += [v]
        
        for w in neighbours(v, graph):
            
            if w not in visited and w not in boundary:
                boundary.append(w)
                dist[w] = dist[v] + 1
        
    return dist

def get_path(parent_list, s, e):
    reversed_path = [e]
    
    while reversed_path[-1] != s:
        v = reversed_path[-1]
        reversed_path.append(parent_list[v])
    
    path = reversed_path[::-1]
    
    return path

def bfs_path(graph, s, goals=[]):
    visited = []
    boundary = [s]
    #############################
    parents = [None] * len(graph)
    #############################
    while len(boundary) > 0:
        v = boundary.pop(0)
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



    

