'''

tag:

21. Merge Two Sorted Lists

Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = sorted(self.to_number(l1)+self.to_number(l2))
        return self.to_linked_list(num)

        
    def to_number (self, l: ListNode):
        number = []
        while(l):
            number.append(l.val)
            l = l.next
        return number

    def to_linked_list(self, number: list):
        if len(number) == 0:
            return 
        head = ListNode(number[0])
        l = head
        for i in range(1, len(number)):
            cur = ListNode(number[i])
            l.next = cur
            l = l.next
        return head
        