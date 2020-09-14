def recursive_boundedlists(lst):

    n = len(lst) 

    if n == 0:
        return [[]]
    
    else:
        smaller = recursive_boundedlists(lst[1:])
        return [[b] + smaller[i] for b in range(lst[0]+1) for i in range(len(smaller))]
