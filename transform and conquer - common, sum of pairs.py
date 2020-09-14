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

    k, n = 1, len(lst)
     
    while k < n:
        
        nxt = []
        
        for a in range(0, n, 2*k):
            b, c = a + k, a + 2*k
            nxt += merge(lst[a:b], lst[b:c])
        
        lst = nxt
        k = 2*k
    
    return lst


def common(a, b):
    lst1 = merge_sort(a) #O(nlog(n))
    lst2 = merge_sort(b) #O(nlog(n))
    final_list = merge(lst1,lst2) #O(n)
    res = [] 
    
    n = len(final_list)
    
    for i in range(n-1):
        if final_list[i] == final_list[i+1]: #O(n)
            res += [final_list[i]] 
    
    return res


# Task 3 
    
from collections import deque 

def pairs_of_sum(lst, s):

    lst2 = [s-x for x in lst]
    
    common_list = deque(common(lst, lst2))
    
 
    res = []
    while len(common_list) > 1:
        a = common_list.popleft()
        b = common_list.pop()
        res.append((a,b))
         
        
    return res