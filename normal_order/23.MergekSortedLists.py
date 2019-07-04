'''

tags: divided and conquer

23. Merge k Sorted Lists

Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            # print(0)
            return
        elif len(lists) == 1:
            # print(1)
            return lists[0]
        elif len(lists) == 2:
            # print(2)
            return self.mergeTwo(lists[0],lists[1])
        else:
            # print('else')
            l1 = self.mergeKLists(lists[:len(lists)//2])
            # print('l1:',l1)
            l2 = self.mergeKLists(lists[len(lists)//2:])
            # print('l2:',l2)
            # print(type(l1),type(l2))
            return self.mergeTwo(l1,l2)
    
    
    def mergeTwo(self,l1,l2):
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
        
        