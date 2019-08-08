'''

24. Swap Nodes in Pairs

Medium

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        ptr = dummy
        while ptr.next and ptr.next.next:
            p1, p2 = ptr.next, ptr.next.next
            ptr.next, p1.next, p2.next, ptr = p2, p2.next, p1, p1
        return dummy.next 
        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        head, head.next = self, head
        print(head)
        # tmp = head
        # head = self
        # head.next = tmp

        while(head.next and head.next.next):
            a = head.next
            b = head.next.next
            head.next, a.next, b.next = b, b.next, a
            head = a
        return self.next

