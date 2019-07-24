'''

tags: Binary Search

222. Count Complete Tree Nodes

Medium

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

'''

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        while root:
            # print(root.val, ans)
            left = self.getHeight(root.left)
            # print(left)
            if left == self.getHeight(root.right):
                root = root.right
                ans += (1<<left) # left side
            else:
                root = root.left
                ans += (1<<(left-1))   # right side
        return ans
    
    def getHeight(self, root):
        ans = 0 
        while root:
            ans += 1
            root = root.left
        return ans