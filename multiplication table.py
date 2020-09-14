def multiplication_table(x):
    table = []
    for j in range(1, x+1):
        row = []
        for i in range(1, x+1):
            row += [i*j]
        table.append(row)
    return table

print(multiplication_table(3))
            
        
