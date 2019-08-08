'''

2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

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
        dummy = ListNode(0)
        ans = dummy
        carry = 0
        while l1 and l2:
            val = l1.val+l2.val+carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            dummy.next = ListNode(val)
            l1, l2, dummy = l1.next, l2.next, dummy.next
            
        while l1:
            val = l1.val + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            dummy.next = ListNode(val)
            l1, dummy = l1.next, dummy.next
            
        while l2:
            val = l2.val + carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            dummy.next = ListNode(val)
            l2, dummy = l2.next, dummy.next 
            
        if carry:
            dummy.next = ListNode(carry)
            dummy = dummy.next
        dummy.next = None
        
        return ans.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.get_num(l1)
        num2 = self.get_num(l2)
        output = num1 + num2
        output = self.get_linked_list(output)
        return output
        
    def get_num(self,ListNode):
        l = ListNode
        digit = l.val
        num = digit
        multiplier = 10
        while l.next:
            l = l.next
            digit = l.val
            num = digit * multiplier + num
            multiplier = multiplier * 10
        return num
    
    def get_linked_list(self,num):
        digit = num % 10
        num = num // 10
        out = ListNode(digit)
        n = out
        while (num != 0):
            digit = num % 10
            num = num // 10
            n.next = ListNode(digit)
            n = n.next
        return out
        
        