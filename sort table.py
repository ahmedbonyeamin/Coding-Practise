def sort_table(table, index):
    for i in range(1, len(table)):
        j = i
    
        while table[j-1][index] > table[j][index] and j > 0:
            table[j], table[j-1] = table[j-1], table[j]
            j = j-1
    return table

