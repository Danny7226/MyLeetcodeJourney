'''

tags: Breadth First Research

101. Symmetric Tree

Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [(root.left, root.right)]
        while(queue):
            node1, node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            elif None in (node1, node2):
                return False
            elif node1.val != node2.val:
                return False
            else:
                queue.append((node1.left, node2.right))
                queue.append((node1.right, node2.left))
                
        return True  