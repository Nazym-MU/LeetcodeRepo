# use recursion

# the base case is when the root is None, which is the end of the tree (leaf's child)

# inorder traversal: left, root, right

def inorderTraversal(root):
  def helper(root):
      if not root:
          return
      helper(root.left)
      res.append(root.val)
      helper(root.right)
  res = [] 
  helper(root)
  return res