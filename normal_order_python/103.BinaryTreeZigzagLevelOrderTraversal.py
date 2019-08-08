'''

103. Binary Tree Zigzag Level Order Traversal

Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, tmp = [], []
        if not root:
            return ans
        bfs = [(root, 0)] # queue
        level_prev = 0
        while bfs:
            cur, level = bfs.pop(0)
            if level == level_prev:
                tmp.append(cur.val)
            else:
                if level_prev % 2:
                    ans.append(tmp[::-1])
                else:
                    ans.append(tmp)
                tmp = [cur.val]
            level_prev = level
            if cur.left:
                bfs.append((cur.left, level+1))
            if cur.right:
                bfs.append((cur.right, level+1))
        if level % 2:
            ans.append(tmp[::-1])
        else:            
            ans.append(tmp)
        return ans
        