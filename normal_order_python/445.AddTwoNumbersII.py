'''

445. Add Two Numbers II

Medium

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.LLToNumber(l1)
        n2 = self.LLToNumber(l2)
        return self.numberToLL(n1+n2)
    
    def LLToNumber(self, l1):
        ans = 0
        while l1:
            ans = ans * 10 + l1.val
            l1 = l1.next
        return ans
    
    def numberToLL(self, n):
        if n == 0:
            return ListNode(0)
        rev = []
        while n:
            n, reminder = divmod(n,10)
            rev.append(reminder)
        dummy = ListNode(0)
        ans = dummy
        while rev:
            dummy.next = ListNode(rev.pop())
            dummy = dummy.next
        dummy.next = None
        return ans.next