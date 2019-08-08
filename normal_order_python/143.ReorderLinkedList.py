'''

143. Reorder List

Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return []
        ll = []
        while head:
            ll.append(head)
            head= head.next
        i, j = 0, len(ll)-1
        # print(ll)
        while i < j-1:
            ll[j].next, ll[i].next = ll[i].next, ll[j]
            i, j = i+1, j-1
        ll[j].next = None
        return ll[0]

    def reorderList(self, head: ListNode) -> None:
        # find mid Node and reverse the 2nd half LL
        # it takes run time O(L)
        l1 = slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        if slow:
            # slow, slow.next = slow.next, None is wrong
            slow.next, slow = None, slow.next
        reverse = None
        while slow:
            reverse, reverse.next, slow = slow, reverse, slow.next
        l2 = reverse
        
        # Merge two half-linked_list
        while l1 and l2:
            l11, l22 = l1.next, l2.next
            l1.next, l2.next = l2, l11
            l1, l2 = l11, l22
