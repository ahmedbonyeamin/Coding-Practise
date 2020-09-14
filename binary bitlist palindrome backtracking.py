def palindrome_binary(n):
    """
    Input: integer n
    Output: list of bitlists in lexicographical order where each bitlist is
            a palindrome.
    
    For Example:
    >>> palindrome_binary(2)
    [[0, 0], [1, 1]]
    >>> palindrome_binary(3)
    [[0, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 1]]
    >>> palindrome_binary(4)
    [[0, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
    """
    def completed(part):
        return len(part) == n
    
    def options(part):
        if len(part) < n/2:
            return [0,1]
        
        else:
            return [part[n - 1 - len(part)]]
        
    def solutions(completed, options, part=[]):

        if completed(part):
            return [part]
        
        else:

            res = []

            for o in options(part):
                augmented = part+[o]
                res += solutions(completed, options, augmented)
            
            return res
    
    
    return solutions(completed, options)