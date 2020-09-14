
"""
Sorted list

for all i, j in range(len(lst)) if i < j then lst[i]<lst[j]

"""
def insert(i, lst):
    
    j = i
    
    while lst[j-1] > lst[j] and j > 0:
        lst[j], lst[j-1] = lst[j-1], lst[j]
        j = j-1

def insertion_sort(lst):
    
    for i in range(1, len(lst)):
        insert(i, lst)
    
    return lst

print(insertion_sort([5,3,2,6,1,8]))

def swap_down(lst, j):
    if lst[j-1] > lst[j]:
        lst[j-1], lst[j] = lst[j], lst[j-1]
    

def shuffle_down(lst, k):
    while k>0 and lst[k-1] > lst[k]:
        lst[k-1], lst[k] = lst[k], lst[k-1]
        k = k-1
        
