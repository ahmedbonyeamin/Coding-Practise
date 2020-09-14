def is_palindrome(string):
    i = 0
    j = -1
    while i < (len(string)/2 + 1):
        if string[i] != string[j]:
            return False
        i = i + 1
        j = j - 1
    return True


def is_palindrome(string):
    length = len(string)
    i = 0
    j = -1
    while i < length//2:
        if string[i] != string[j-i]:
            return False
        i += 1
    return True