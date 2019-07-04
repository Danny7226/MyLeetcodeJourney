'''

145. Binary Tree Postorder Traversal

Hard

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []        
        if not root:
            return ans
        stack = [(root, False)]
        while stack:
            cur, visited = stack.pop()
            if not cur:
                continue
            if visited:
                ans.append(cur.val)
            else:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))
        return ans

        
class Solution:        
    def __init__(self):
        self.ans = []
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return self.ans
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.ans.append(root.val)     
        return self.ans        