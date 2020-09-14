def rpermutations(lst):
    """ Generates all permutations of input list.
    
    >>> sorted(rpermutations(list(range(1, 4))))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(rpermutations(list(range(1, 5))))
    [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
    >>> sorted(rpermutations(list('JOE')))
    [['E', 'J', 'O'], ['E', 'O', 'J'], ['J', 'E', 'O'], ['J', 'O', 'E'], ['O', 'E', 'J'], ['O', 'J', 'E']]

    <Write your explanation here>
    """
    n = len(lst)

    if n == 0:
        return [[]]

    else:
        permutations = rpermutations(lst[1:])
        item = lst[0]  
        return [perm[:i] + [item] + perm[i:] for i in range(len(permutations[0])+1) for perm in permutations]