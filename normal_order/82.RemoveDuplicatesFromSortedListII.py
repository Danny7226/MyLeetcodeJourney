'''

82. Remove Duplicates from Sorted List II

Medium

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3


'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        ans = tmp = dummy
        while dummy and dummy.next:
            mark = dummy.val
            # print(mark)
            if dummy.next.val != mark:
                tmp, dummy = dummy, dummy.next
            else:
                while dummy.next and dummy.next.val == mark:
                    dummy = dummy.next
                dummy = dummy.next
                tmp.next = dummy
        return ans.next