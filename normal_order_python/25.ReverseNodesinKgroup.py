'''

25. Reverse Nodes in k-Group

Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # run time O(L), space O(1)
    def reverseKGroup(self, head, k):
        if k == 0:
            return head
        cur = ListNode(None)
        cur.next = head
        ans = cur
        while cur != -1:
            cur = self.reverseK(cur,k)
        return ans.next
        
    def reverseK(self, cur, k):
        count = 0
        pre = cur
        index = start = cur.next
        rev = None
        while cur.next and count != k:
            cur = cur.next
            count += 1
        if count == k:
            if cur:
                nxt = cur.next
                while count:
                    rev, rev.next, index = index, rev, index.next
                    count -= 1
                pre.next, start.next = rev, nxt
            else:
                while count:
                    rev, rev.next, index = index, rev, index.next
                    count -= 1
                pre.next = rev
            return start
        else:
            return -1