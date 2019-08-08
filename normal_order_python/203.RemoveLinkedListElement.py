'''

tags: Linked List

203. Remove Linked List Elements

Easy

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: # return None when its a empty linked list
            return 

        while head and head.val == val: # find the fist Node which value is not 'val'
            head = head.next

        # if head: # when head is not the tail
        #     self, head = head, head.next
        # else: # when head is the tail
        #     self = head

        pre = self = head
        while head:
            if head.val == val:
                if head.next: # when head is not the tail
                    pre.next = head.next
                else: # when head is the tail
                    pre.next = None
                head = pre.next
            else:
                pre, head = head, head.next
            
        return self