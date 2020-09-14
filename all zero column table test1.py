def contains_all_zero_col(table):
    
    for j in range(len(table[0])):
        check = True
        
        for i in range(len(table)):
            
            if table[i][j] != 0:
                check = False
        
        if check == True:
            return check
            
    return check