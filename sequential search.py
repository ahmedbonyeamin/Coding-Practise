def sequential_search(v, seq):
    for i in range(len(seq)):
        if seq[i] == v:
            return i
    return None
        
    