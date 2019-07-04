'''

61. Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        nxt = head
        leng = 1
        while head.next:
            head = head.next
            leng += 1
        head.next = nxt
        k = k % leng
        cut = leng - k - 1
        for _ in range(cut):
            nxt = nxt.next
        ans, nxt.next = nxt.next, None
        return ans

# class Solution:
#     # very slow
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if not head or not head.next:
#             return head
#         leng = 0
#         temp = head
#         while temp:
#             temp = temp.next
#             leng+=1
#         # print(leng)
#         k = k % leng
#         def rotate(head):
#             tmp = head
#             ptr1, ptr2 = head, head.next
#             while ptr2.next:
#                 ptr1, ptr2 = ptr2, ptr2.next
#             ptr1.next, ptr2.next, head = None, tmp, ptr2
#             return head
#         while k:
#             head = rotate(head)
#             k -= 1
#         return head
