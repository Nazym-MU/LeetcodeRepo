# using recursion
def shortestToChar(s, c):
    # base case
    def recursion(i, distance):
        if i < 0 or i >= len(s) or result[i] < distance:
            return        
    
        result[i] = distance
        recursion(i-1, distance+1)
        recursion(i+1, distance+1)
    result = [len(s) for i in range(len(s))]
    for i, ch in enumerate(s):
        if ch == c:
            recursion(i, 0)
    return result