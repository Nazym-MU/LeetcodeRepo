# use recursion

# if the root has only one child, return the depth of the existing subtree.
# if both exist, return the minimum depth of the two subtrees.

def minDepth(self, root):
  if not root: 
      return 0 
  elif root.left and root.right:
      return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
  elif root.left:
      return 1 + self.minDepth(root.left)
  else:
      return 1 + self.minDepth(root.right)