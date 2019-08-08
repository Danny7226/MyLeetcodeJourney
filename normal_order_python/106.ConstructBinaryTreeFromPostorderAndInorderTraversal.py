'''

106. Construct Binary Tree from Inorder and Postorder Traversal

Medium

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            # print(inorder, postorder)
            root_val = postorder.pop() # time consuming
            root = TreeNode(root_val)
            pos = inorder.index(root_val)
            root.right = self.buildTree(inorder[pos+1:], postorder)
            root.left = self.buildTree(inorder[:pos], postorder)
            return root

