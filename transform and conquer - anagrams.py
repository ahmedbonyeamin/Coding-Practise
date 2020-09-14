"""ANAGRAMS TRANSFORM AND CONQUER"""

def order_invariant_indexing(lst):
    res = []
    
    for word in lst:
        sorted_letters = sorted(word)
        key = ''
        for letter in sorted_letters:
            key += letter
        res.append((key, word))
    return res


def anagrams(words):
    
    augmented = order_invariant_indexing(words)
    ordered = sorted(augmented)
    
    res = []
    i = 0
    while i < len(ordered):
        res.append([])
        key = ordered[i][0]
        
        while i < len(ordered) and ordered[i][0] == key:
            res[-1].append(ordered[i][1])
            i = i+1
            
    return res

print(anagrams(['solver', 'camera', 'waster', 'typhon', 'tawers', 'lovers', 'waters', 'higher', 'python', 'rawest']))



