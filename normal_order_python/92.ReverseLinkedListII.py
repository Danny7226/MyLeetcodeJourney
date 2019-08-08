'''

92. Reverse Linked List II

Medium

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        ans = dummy
        pos = 1
        while m != 1:
            m -= 1
            pos += 1
            dummy = dummy.next
        first = dummy
        second = dummy.next
        dummy = dummy.next
        rev = None
        while pos != n+1:
            rev, rev.next, dummy = dummy, rev, dummy.next
            pos += 1
        first.next, second.next = rev, dummy
        return ans.next
        
        
        
        