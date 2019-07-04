'''

tags: DFS

872. Leaf-Similar Trees

Easy

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1 = self.DFS(root1)
        leaf2 = self.DFS(root2)
        return leaf1 == leaf2
        
    def DFS(self, root):
        ans = []
        if not root:
            return ans  
        dfs = [] # stack
        dfs.append(root)
        while dfs:
            root = dfs.pop()
            if not root.left and not root.right:
                ans.append(root.val)
            if root.right:
                dfs.append(root.right)
            if root.left:
                dfs.append(root.left)
        return ans