'''

148. Sort List

Medium

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        l1, l2 = self.findMid(head)
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.mergeList(l1,l2)
        
    def findMid(self, head):     
        dummy = ListNode(None)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        slow.next, slow = None, slow.next
        return (dummy.next, slow)
    
    def mergeList(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        dummy = ListNode(None)
        ans = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1, dummy = l1.next, dummy.next
            else:
                dummy.next = l2
                l2, dummy = l2.next, dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return ans.next