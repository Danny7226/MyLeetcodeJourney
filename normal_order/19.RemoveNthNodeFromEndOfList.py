'''

tag: 

19. Remove Nth Node From End of List

Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# two pass solution: 40ms, faster than 92.29%
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        leng = 0
        loop = head
        while (loop):
            leng += 1
            loop = loop.next

        cut = leng - n
               
        tmp = head
        if (cut == 0):
            return head.next
        for i in range(cut-1):
            tmp = tmp.next
        tmp.next = tmp.next.next
        return head

# class Solution:
#     def removeNthFromEnd(self, head, n):
#         fast = slow = head
#         for _ in range(n):
#             fast = fast.next
#         if not fast:
#             return head.next
#         while fast.next:
#             fast = fast.next
#             slow = slow.next
#         slow.next = slow.next.next
#         return head
