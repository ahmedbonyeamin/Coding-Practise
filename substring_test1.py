def substring(string, ch):
    
    for i in range(len(string)-1):
        
        if string[i] == ch:
            
            n = i+1
            
            while string[n] != ch and n<len(string):
                n += 1
            
            if string[n] == ch:
                return string[i:n+1]
            
    return None

string = "wwklmonw$%^&www"
ch= "w"

print(substring(string, ch))
