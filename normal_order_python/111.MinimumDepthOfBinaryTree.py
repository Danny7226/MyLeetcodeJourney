'''

111. Minimum Depth of Binary Tree

Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        Min = float('inf')
        stack = [(1, root)]
        while(stack):
            depth, node = stack.pop()
            if not node:
                continue
            elif not node.left and not node.right:
                if depth < Min:
                    Min = depth
                continue
            else:
                stack.append((depth+1, node.left))
                stack.append((depth+1, node.right))
        return Min