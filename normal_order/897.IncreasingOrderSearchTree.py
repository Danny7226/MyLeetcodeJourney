'''

897. Increasing Order Search Tree

Easy

Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

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
            \
             7
              \
               8
                \
                 9  
'''                 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right  

class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        LFS = self.LFS(root)
        ans = LFS[0]
        for i in range(len(LFS)-1):
            LFS[i].left = None
            LFS[i].right = LFS[i+1]
        LFS[-1].left = None
        return ans
    
    def LFS(self,root):
        if not root:
            return []
        return self.LFS(root.left) + [root] + self.LFS(root.right)
        
                  