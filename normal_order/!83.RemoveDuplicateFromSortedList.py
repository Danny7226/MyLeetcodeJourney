'''

tags: linked list

83. Remove Duplicates from Sorted List

Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''
linked_list = [1,1,2,3,3,4,4,5,5,6,7,9]
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(head):
        output = []
        while(head):
            output.append(head.val)
            head = head.next
        print(output)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        output = head
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return output

class Solution:
    # one pass solution
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ptr1 = head
        ptr2 = head
        if not head:
            return
        while(ptr2):
            if ptr2.val == ptr1.val:
                ptr2 = ptr2.next
            else:
                ptr1 = ptr1.next
                ptr1.val = ptr2.val
                ptr2 = ptr2.next
        ptr1.next = None
        return head


# main code starts
x = ListNode(linked_list[0])
head = x
for i in range(1,len(linked_list)):
    x.next = ListNode(linked_list[i])
    x = x.next
ListNode.print(head)
s = Solution()
head2 = s.deleteDuplicates(head)
ListNode.print(head2)


