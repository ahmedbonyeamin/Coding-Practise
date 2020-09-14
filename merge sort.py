def mergesort(lst):
    
    n = len(lst)
    k = 1
    
    while k < n:
        
        nxt = []
        
        for a in range(0, n, 2*k):
            b,c = a + k, a + 2*k
            nxt += merge(lst[a:b], lst[b:c])
            
        lst = nxt
        k = k*2
    
    return lst

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

def insert(i, lst):
    
    j = i
    
    while lst[j-1] > lst[j] and j > 0:
        lst[j], lst[j-1] = lst[j-1], lst[j]
        j = j-1
        
def insertion_merge(lst1, lst2):
    
    n1, n2 = len(lst1), len(lst2)
    res = lst1 + lst2
    
    for i in range(n1, n1 + n2):
        insert(i, res)
    return res

