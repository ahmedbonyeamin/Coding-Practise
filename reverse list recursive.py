def reverse_list(lst):
    n = len(lst)
    
    if len(lst) <= 1:
        return lst
        
    else:
        return [lst[-1]] + reverse_list(lst[:-1])


print(reverse_list([1,2,3,4,5]))

def reverse(lst):
    
    n = len(lst)
    
    if n <= 1:
        return lst
    
    else:
        return reverse(lst[1:]) + [lst[0]]
    
    
    