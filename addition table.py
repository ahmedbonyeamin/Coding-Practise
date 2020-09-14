def addition_table(lst):
    table = []
    for i in range(1,4):
        
        
        row = []
        
        for num in lst:
            row.append(num + i)
        table.append(row)
        
    return table
