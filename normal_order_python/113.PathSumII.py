'''

113. Path Sum II

Medium

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # iterative
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        stack = [(root, root.val, [root.val])] # stack stored with (root, sum, path)
        while stack:
            cur, Sum, path = stack.pop()
            if not cur.left and not cur.right:
                if Sum == sum:
                    ans.append(path)
            else:
                if cur.right:
                    stack.append((cur.right, Sum+cur.right.val, path+[cur.right.val]))                
                if cur.left:
                    stack.append((cur.left, Sum+cur.left.val, path+[cur.left.val]))
        return ans

class Solution:
    # recursive
    
    def __init__(self):
        self.ans = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.sum = sum
        if not root:
            return self.ans
        self.helper([root.val], root, root.val)
        return self.ans
    def helper(self, path, root, Sum):
        # print(path, root.val, Sum)
        if not root.left and not root.right:
            if Sum == self.sum:
                self.ans.append(path)
        else:
            if root.left:
                self.helper(path+[root.left.val], root.left, Sum+root.left.val)
            if root.right:
                self.helper(path+[root.right.val], root.right, Sum+root.right.val)
