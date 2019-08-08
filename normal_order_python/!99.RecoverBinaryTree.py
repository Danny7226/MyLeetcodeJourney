'''

99. Recover Binary Search Tree

Hard

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # iterative
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [(root, False)]
        first, second, prev = None, None, TreeNode(-float('inf'))
        while stack:
            cur, visited = stack.pop()
            # print(cur.val, visited, end = ' ')
            if visited:
                if cur.val < prev.val:
                    if not first:
                        first = prev
                    second = cur
                prev = cur
                continue
            if cur.right:
                stack.append((cur.right, False))
                
            stack.append((cur, True))
            
            if cur.left:
                stack.append((cur.left, False))
            # print(stack)
        
        first.val, second.val = second.val, first.val

class Solution:
    
    def __init__(self):
        self.first, self.second = None, None
        self.prev = TreeNode(-float('inf'))
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if not self.first and self.prev.val > root.val:
            self.first, self.second = self.prev, root
        if self.first and self.prev.val > root.val:
            self.second = root
        self.prev = root
        self.inorder(root.right)