weights = [4, 9, 10, 20, 2, 1]
values = [400, 1800, 3500, 4000, 1000, 200]        
capacity = 20

"""GREEDY APPROACH"""

"""PRIORITIZE HIGH VALUE ITEMS"""

def greedy_knapsack(values, weights, capacity):
    n = len(values)
    
    def score(i):
        return values(i)
    
    items = sorted(range(n), key = score, reverse = True)

    res = []
    value = 0
    weight = 0

    for i in items:
        if weight + weights[i] <= capacity:
            res.append(i)
            value += values[i]
            weight += weight[i]
    
    return res, value, weight

"""PRIORITIZE LOW WEIGHT ITEMS"""

def greedy_knapsack(values, weights, capacity):
    n = len(values)
    
    def score(i):
        return weights[i]
    
    items = sorted(range(n), key = score)
    
    res = []
    value = 0
    weight = 0
    
    for i in items:
        if weight + weights[i] <= capacity:
            res += [i]
            value += values[i]
            weight += weights[i]
    
    return res, value, weight

"""Prioritize high value per kg"""

def greedy_knapsack(values, weights, capacity):
    n = len(values)
    
    def score(i):
        return values[i]/weights[i]
    
    items = sorted(range(n), key = score, reverse = True)
    
    res = []
    value = 0
    weight = 0
    
    for i in items:
        if weight + weights[i] <= capacity:
            res += [i]
            value += values[i]
            weight += weights[i]
    
    return res, value, weight
