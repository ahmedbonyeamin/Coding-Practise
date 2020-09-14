def sum_of_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])