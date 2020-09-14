def remove_neg(lst):
    if len(lst) == 0:
        return []
    if lst[0] >= 0:
        return [lst[0]] + remove_neg(lst[1:])
    else:
        return remove_neg(lst[1:])
    
print(remove_neg([2, 5, 3, -7, 10]))