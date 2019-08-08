'''

889. Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not post:
            return None
        elif len(post) == 1:
            return TreeNode(pre.pop(0))
        else:
            root = TreeNode(pre.pop(0))
            # print(root.val)
            pos = post.index(pre[0])
            root.left = self.constructFromPrePost(pre, post[:pos+1])
            root.right = self.constructFromPrePost(pre, post[pos+1:-1])
            return root