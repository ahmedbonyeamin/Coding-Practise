def merge(lst1, lst2):
    
    n1, n2 = len(lst1), len(lst2)
    
    i, j = 0, 0
    
    res = []
    while i < n1 and j < n2:
        
        if lst1[i] <= lst2[j]:
            res += [lst1[i]]
            i += 1
        
        else:
            res += [lst2[j]]
            j += 1
    
    return res + lst1[i:] + lst2[j:]


def merge_sort(lst):
    n = len(lst)
    
    if n <= 1:
        return lst
    
    else:
        sub1 = merge_sort(lst[:n//2])
        sub2 = merge_sort(lst[n//2:])
        return merge(sub1, sub2)
    
print(merge_sort([1,1,22,22,3,4,5,5,33,22,1,5])) 