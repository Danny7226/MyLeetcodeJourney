'''

173. Binary Search Tree Iterator

Medium

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.iterator = []
        self.stack = []
        if root:
            self.stack.append(root)
        while self.stack:
            cur = self.stack.pop()
            self.iterator.append(cur.val)
            if cur.right:
                self.stack.append(cur.right)
            if cur.left:
                self.stack.append(cur.left)
        if self.iterator:
            self.iterator.sort(reverse = True)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.iterator.pop()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.iterator:
            return True
        else:
            return False

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        
        self.helper(root)
        
    def helper(self,root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        root = self.stack.pop()
        if root.right:
            self.helper(root.right)
        return root.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()