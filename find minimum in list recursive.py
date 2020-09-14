def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], find_min(lst[1:]))

print(find_min([5,7,8,-5,10]))