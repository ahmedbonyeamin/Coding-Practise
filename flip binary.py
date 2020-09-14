def flip(binary_string):
    index = 0
    new_binary = ''
    while index < len(binary_string):
        if binary_string[index] == '0':
            new_binary = new_binary + '1'
        elif binary_string[index] == '1':
            new_binary = new_binary + '0'
        index = index + 1
    return new_binary

age = 21

print(f"I am {str(age)} years old")



