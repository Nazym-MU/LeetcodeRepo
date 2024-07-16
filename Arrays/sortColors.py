'''
Dutch partitioning problem
   l         h
1) 2,0,2,1,1,0
   m
   l       h
2) 0,0,2,1,1,2
   m
       l   h
3) 0,0,2,1,1,2
       m
       l h
4) 0,0,1,1,2,2
       m
       l h
5) 0,0,1,1,2,2
         m
'''

def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

'''
Time: O(n)
Space: O(1)
'''