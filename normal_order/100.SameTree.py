'''

tags: Depth-first-research

100. Same Tree

Easy

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def search(root):
            if(root == None):
                output.append('null')               
            else:
                output.append(root.val)
                search(root.left)  
                search(root.right)
        output = []
        search(p)
        tree1 = output
        output = []
        search(q)
        tree2 = output
        return tree1 == tree2

x = TreeNode(1)
p = x
x.left, x.right = TreeNode(2), TreeNode(3) 

x = TreeNode(1)
q = x
x.left, x.right = TreeNode(2), TreeNode(3) 

s = Solution()
print(s.isSameTree(p,q))