'''

234. Palindrome Linked List

Easy

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

'''

class Solution:
	# O(L) time, O(n) extra space
    def isPalindrome(self, head: ListNode) -> bool:
        check = []
        if not head:
            return True
        while head:
            check.append(head.val)
            head = head.next
        return check == check[::-1]

    # O(L) time, O(1) extra space
    def isPalindrome(self, head: ListNode) -> bool:
    slow = fast = head
    reverse = None
    while fast and fast.next:
        reverse, reverse.next, slow, fast = slow, reverse, slow.next, fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if slow.val == reverse.val:
            slow, reverse = slow.next, reverse.next
        else:
            return False
    return True