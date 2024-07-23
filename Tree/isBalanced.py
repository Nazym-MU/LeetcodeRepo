# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        return (self.helper(root) >= 0)
    def helper(self, root):
        if not root:
            return 0
        leftHeight, rightHeight = self.helper(root.left), self.helper(root.right)
        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1: 
            return -1
        return max(leftHeight, rightHeight) + 1

# Time: O(n)
# Space: O(n)