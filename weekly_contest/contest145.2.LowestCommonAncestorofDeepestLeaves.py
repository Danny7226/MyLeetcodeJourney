'''

1123. Lowest Common Ancestor of Deepest Leaves

Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.
 

Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Explanation: 
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".
Example 2:

Input: root = [1,2,3,4]
Output: [4]
Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]
 

Constraints:

The given tree will have between 1 and 1000 nodes.
Each node of the tree will have a distinct value between 1 and 1000.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        bfs = [(root, 0)] # queue
        self.parent = {root: None}
        layer, depth_prev = [], 0
        while bfs:
            cur, depth = bfs.pop(0)
            if depth == depth_prev:
                layer.append(cur)
            else:
                layer = [cur]
            depth_prev = depth    
            if cur.left:
                bfs.append((cur.left, depth+1))
                self.parent[cur.left] = cur            
            if cur.right:
                bfs.append((cur.right, depth+1))
                self.parent[cur.right] = cur
        node = layer.pop()
        return self.find(node, layer)
        
    def find(self, node, layer):
        if not layer:
            return node
        else:
            node2 = layer.pop() # 2
        tmp = set()
        tmp.add(node)
        while self.parent[node]:
            tmp.add(self.parent[node])
            node = self.parent[node]
        while not self.parent[node2] in tmp:
            node2 = self.parent[node2]
        node2 = self.parent[node2]
        return self.find(node2, layer)
        