def simplify(string):
    
    if len(string) <= 1:
        return string
    
    if len(string) > 1 and string[0] == string[1]:
        return simplify(string[1:])
    else:
        return string[0] + simplify(string[1:])
    
print(simplify('fffggsd'))