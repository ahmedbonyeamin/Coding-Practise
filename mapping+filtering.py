""" Function as parameter"""

def list_from_file(filename, typ=str):
    file = open(filename)
    res = []
    for line in file:
        res = res + [typ(line.strip())]
        #str()
    file.close()
    return res


"""Mapping"""

lst = ["1", "2", "3"]

lst2 = list(map(float, lst))

print(lst2)


"""Filter"""

filter(function, sequence)

"""a list of elements from seq that when used as input in 
#function returns True"""

