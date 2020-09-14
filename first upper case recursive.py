def first_upper(string):
    
    if len(string) == 1:
        return string[0].isupper()
    
    if string[0].isupper():
        return string[0]
    
    else:
        return first_upper(string[1:])


print(first_upper('abC yz'))    
    