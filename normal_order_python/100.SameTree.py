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
    	# DFS
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
        
# # DFS with stack        
# def isSameTree2(self, p, q):
#     stack = [(p, q)]
#     while stack:
#         node1, node2 = stack.pop()
#         if not node1 and not node2:
#             continue
#         elif None in [node1, node2]:
#             return False
#         else:
#             if node1.val != node2.val:
#                 return False
#             stack.append((node1.right, node2.right))
#             stack.append((node1.left, node2.left))
#     return True
 
# # BFS with queue    
# def isSameTree3(self, p, q):
#     queue = [(p, q)]
#     while queue:
#         node1, node2 = queue.pop(0)
#         if not node1 and not node2:
#             continue
#         elif None in [node1, node2]:
#             return False
#         else:
#             if node1.val != node2.val:
#                 return False
#             queue.append((node1.left, node2.left))
#             queue.append((node1.right, node2.right))
#     return True

x = TreeNode(1)
p = x
x.left, x.right = TreeNode(2), TreeNode(3) 

x = TreeNode(1)
q = x
x.left, x.right = TreeNode(2), TreeNode(3) 

s = Solution()
print(s.isSameTree(p,q))