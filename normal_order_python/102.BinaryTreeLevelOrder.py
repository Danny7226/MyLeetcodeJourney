'''

102. Binary Tree Level Order Traversal

Medium

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, tmp, level_prev = [], [], 0
        if not root:
            return ans
        BFS = [(root, 0)] # queue
        while BFS:
            cur, level = BFS.pop(0)
            if level != level_prev:
                ans.append(tmp)
                tmp = []
            tmp.append(cur.val)
            level_prev = level
            if cur.left:
                BFS.append((cur.left, level+1))
            if cur.right:
                BFS.append((cur.right, level+1))
        ans.append(tmp)
        return ans