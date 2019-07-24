'''


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	# much faster
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        stack = [root] 
        parent = {root:None}
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
                parent[cur.right] = cur
            if cur.left:
                stack.append(cur.left)
                parent[cur.left] = cur
            if p in parent and q in parent:
                break
        # print(parent)
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]
        while q not in ancestor:
            q = parent[q]
        return q

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        stack = [(root, [root])] # stack stored with current node and path
        two = {}
        while stack:
            cur, path = stack.pop()
            if cur == p:
                # print(path)
                two[p] = path+[cur]
            if cur == q:
                # print(path)
                two[q] = path+[cur]
            if len(two) == 2:
                break
            if cur.right:
                stack.append((cur.right, path+[cur]))
            if cur.left:
                stack.append((cur.left, path+[cur]))
        # print(two[p])
        return [x for x in two[p] if x in two[q]][-1]
