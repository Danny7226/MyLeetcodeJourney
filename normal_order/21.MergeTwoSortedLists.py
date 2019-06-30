'''

tag: linked list

21. Merge Two Sorted Lists

Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            output = l1 or l2
            return output
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
            
class Solution:    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            output = l1 or l2
            return output
        p, q = l1, l2
        tmp = output = ListNode(None)
        while p and q:
            if p.val <= q.val:
                tmp.next, p = p, p.next
                tmp = tmp.next
            else:
                tmp.next, q = q, q.next
                tmp = tmp.next
        if q:
            tmp.next = q
        else:
            tmp.next = p
        return output.next