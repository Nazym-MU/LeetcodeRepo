# recursively get the root, which is the middle index of the list
# then recursively call the function with the left half and the right half
# the base case is when the list is empty
# return the root of the tree at the end

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return 
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

# Time: O(n) -> we're visiting each value in the array to create a BST
# Space: O(n) -> initializing an array