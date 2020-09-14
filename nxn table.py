def table(n):
    table = []
    for j in range(n):
        row = []
        for i in range(n):
            row += [i + j]
        table.append(row)
    
    return table

print(table(3))