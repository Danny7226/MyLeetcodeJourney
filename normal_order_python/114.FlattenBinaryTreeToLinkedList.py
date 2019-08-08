'''

114. Flatten Binary Tree to Linked List

Medium

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    dummy = TreeNode(None)
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = self.dummy
        self.MFS(root)
    
    def MFS(self,root):
        if not root:
            return
        # print(root.val)
        self.dummy.left = None
        self.dummy.right = root
        self.dummy = root
        l, r = root.left, root.right
        self.MFS(l)
        self.MFS(r)
            
        
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dfs = []
        dfs.append(root)
        while root and dfs:
            root = dfs.pop()
            if root.right:
                dfs.append(root.right)
            if root.left:
                dfs.append(root.left)
                root.right = root.left
                root.left = None
            else:
                if dfs:
                    root.right = dfs[-1]
                    root.left = None
        
            
        