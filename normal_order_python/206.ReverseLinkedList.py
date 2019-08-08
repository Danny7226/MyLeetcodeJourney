'''

206. Reverse Linked List

Easy

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''

class Solution:
    # iteratively
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        ptr = head
        while ptr:
            reverse, reverse.next, ptr = ptr, reverse, ptr.next
        return reverse

class Solution:
    # recursively
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        N = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return N        