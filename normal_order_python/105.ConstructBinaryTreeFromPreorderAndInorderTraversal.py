'''

105. Construct Binary Tree from Preorder and Inorder Traversal

Medium

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return
        root_val = preorder.pop(0)
        pos = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder, inorder[:pos])
        root.right = self.buildTree(preorder, inorder[pos+1:])     
        return root