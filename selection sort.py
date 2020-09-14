"""
Sorted list

for all i, j in range(len(lst)) if i < j then lst[i]<lst[j]

"""
def min_index(lst):
    
    my_min = 0
    
    for i in range(len(lst)):
        if lst[i] < lst[my_min]:
            my_min = i
    return my_min

def selection_sort(lst):
    
    for i in range(len(lst)-1):
        j = min_index(lst[i:])+i
        lst[i], lst[j] = lst[j], lst[i]
        
    return lst

print(selection_sort([5,3,2,6,1,8]))


def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]


def find_min(lst, index):
    min_val = lst[index:][0]
    min_position = 0
    for i in range(len(lst[index:])):
        if lst[index:][i] < min_val:
            min_val = lst[index:][i]
            min_position = i
    res = min_position + index
    return res
        

# selection sort
def selection_sort(lst):
    for i in range(len(lst) - 1):
        minimum_index = find_min(lst,i)
        swap(lst,i,minimum_index)
            
    