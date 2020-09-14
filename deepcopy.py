def deepcopy_exactly_2(lst):
    new = []
    for n in range (len(lst)):
        new.append([])
    for i in range (len(lst)):
        for j in range (len(lst[i])):
            new[i].append(lst[i][j])
    return new

print(deepcopy_exactly_2( ))


def deepcopy_atmost2(lst):
    new = []
    
    for n in range(len(lst)):
        new.append(None)
        
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            new[i] = []
            
            for j in range(len(lst[i])):
                new[i]. append(lst[i][j])
        
        else:
            new[i] = lst[i]
    return new 