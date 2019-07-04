'''

94. Binary Tree Inorder Traversal

Medium

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # iterative      
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans


class Solution:
    # recursive
    def __init__(self):
        self.ans = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.LFS(root)
        return self.ans
        
    def LFS(self,root):
        if not root:
            return
        self.LFS(root.left)
        self.ans.append(root.val)
        self.LFS(root.right)