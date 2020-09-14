seq = [3, 5, 2, 1, -3]

def minimum_difference(lst):
    lst1 = sorted(lst) #nlogn
    
    res = (lst1[0], lst1[1])
    value = abs(lst1[0]-lst1[1])
    
    for i in range(len(lst1)-1):
        if abs(lst1[i]-lst1[i+1]) < value:
            res = (lst1[i], lst1[i+1])
            value = abs(lst1[i]-lst1[i+1])
    return res

print(minimum_difference(seq))

