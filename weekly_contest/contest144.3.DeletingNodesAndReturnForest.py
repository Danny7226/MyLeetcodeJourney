'''

1110. Delete Nodes And Return Forest

Medium

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

Example 1:

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        parent = {root:(None, 0)}
        queue = [root]
        key = set(to_delete)
        ans = [root]
        while queue:
            cur = queue.pop(0)
            if cur.val in key:
                if parent[cur][0]:
                    if parent[cur][1]:
                        parent[cur][0].right = None
                    else:
                        parent[cur][0].left = None
                else:
                    ans = []
                if cur.left and cur.left.val not in key:
                    ans.append(cur.left)
                if cur.right and cur.right.val not in key:
                    ans.append(cur.right)
            if cur.left:
                queue.append(cur.left)
                parent[cur.left] = (cur, 0)
            if cur.right:
                queue.append(cur.right)
                parent[cur.right] = (cur, 1)
        return ans