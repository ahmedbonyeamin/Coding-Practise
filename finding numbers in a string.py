string = ??
numbers = ['0','1','2','3','4','5','6','7','8','9']
i = 0
sum = 0
while i < len ( string ):
    if string [ i ] in numbers :
        j = i
        while j < len ( string ) and string [ j ] in numbers :
            j = j +1
        num = string [ i : j ]
        sum = sum + int ( num )
        i = j
        i = i + 1
        