def merge(lst1, lst2):

    n = len(lst1)
    
    m = len(lst2)
    
    res = []
    
    i = 0
    
    j = 0
    
    while i < n and j < m:
        
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


'''TRANSFORM AND CONQUER UNIQUE VALUES'''    

def unique_values(lst):
    n = len(lst)
    lst = merge_sort(lst)
    res = [lst[0]]
    
    for i in range(1, n):
        if lst[i] != lst[i-1]: 
            res.append(lst[i]) 
    
    return res

print(unique_values([1,1,22,22,3,4,5,5,33,22,1,5]))

