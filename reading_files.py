file = open()
content = []

for line in file:
    content += [line]
    
file.close()

def list_from_file(filename):
    file = filename.open()
    
    res = []
    
    for line in file:
        res += [line.strip()]
    file.close()
    return res

"""Numeric Type conversion"""

def list_from_file(filename, num=False):
    file = filename.open()
    
    res = []
    
    for line in file:
        if num:
            res += [float(line.strip())]
        else:    
            res += [line.strip()]
    file.close()
    return res

def quantity_eaten(food, food_diary):
   
    res = 0
    for row in food_diary:
        if row[0] == food:
            res += row[1]
    return res

def quantity_eaten(food, food_diary):
   
    res = 0
    for f,q in food_diary:
        if f == food:
            res += q
    return res

def word_from_file(file):
    f = open(file)
    for line in f:
        if len(line.strip()) != 0:
            first_line = line
            break
    
    first_line_list = first_line.split()
   
    first_word = first_line_list[0]
    f.close()
    return first_word

def nested_int_list_from_file(file):
    f = open(file)
    table = []
    for line in f:
        row = line.split(',')
        lst = []
        for j in range(len(row)):
            lst.append(int(row[j].strip()))
        table.append(lst)
    f.close()
    return table
        
    