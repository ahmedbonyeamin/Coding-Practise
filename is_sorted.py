def is_sorted(seq):
    
    for i in range(len(seq)-1):
        if seq[i+1] > seq[i]:
            return False
    return True
