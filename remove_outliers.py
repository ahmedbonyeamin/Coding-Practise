def remove_outliers(table):
    minimum = table[0][0]
    maximum = table[0][0]
    for i in range(len(table)):
        
        for j in range(len(table[0])):
            
            if table[i][j] > maximum:
                maximum = table[i][j]
            if table[i][j] < minimum:
                minimum = table[i][j]
    mid = (minimum + maximum) / 2
    for i in range(len(table)):
        
        for j in range(len(table[0])):
            
            if table[i][j] == minimum or table[i][j] == maximum:
                table[i][j] =  mid
    return table

print(remove_outliers([[0,4],[2,4],[-1,3]]))