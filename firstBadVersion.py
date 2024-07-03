'''
Suppose you have n versions [1, 2, ..., n] 

Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

      r   l   
1, 2, 3, 4, 5,
      F  
         T
bad = 4


'''
# 1 , 2, 3, 4, 5

# 1. initialize two pointers: left and right
# 2. while left <= right
# 3. find the middle index, call isBadVersion()
# 4. if true, right = middle - 1
# 5. else left = middle + 1

def firstBadVersion(n):
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


'''
Time: O(logn)
Space: O(1)
'''