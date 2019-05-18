'''

107. Binary Tree Level Order Traversal II

Easy

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        output = [[]]
        level_cur = 1
        queue = [(level_cur, root)]
        tmp = []
        while (queue):
            level_cur, node = queue.pop(0)
            if node != None:
                if len(output) < level_cur:
                    output.insert(0,[])
                    output[-level_cur].append(node.val)
                    # !!!output[-level] counts from the end

                else:
                    output[-level_cur].append(node.val)
                queue.append((level_cur+1, node.left))
                queue.append((level_cur+1, node.right))
            else:
                continue
        return output