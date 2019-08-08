'''


tags: 2 ptrs

142. Linked List Cycle II

Medium

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow up:
Can you solve it without using extra space?

'''
linked_list = [3,2,0,-4]
# Definition for singly-linked list.
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
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        hash_table = set()
        while head:
            if head not in hash_table:
                hash_table.add(head)
                head = head.next
            else:
                return head
        return None

class Solution:
    # @param head, a ListNode
    # @return a list node

    # If fast and slow both start at head, when fast catches slow, slow has traveled H+D and fast 2(H+D). 
    # Assume fast has traveled n loops in the cycle, we have:
    # 2H + 2D = H + D + nL  -->  H + D = nL  --> H = nL - D    
    def detectCycle(self, head):
        if not head:
            return
        slow  = head
        fast = head.next
        while fast and fast.next and fast != slow:
            slow, fast = slow.next, fast.next.next
        if fast == slow:
            slow = slow.next
            while head != slow:
                head, slow = head.next, slow.next
            return slow
        else:
            return     

head = ListNode(linked_list[0])
x = head
for i in range(1,len(linked_list)):
    x.next = ListNode(linked_list[i])
    x = x.next
y = head
y = y.next
# ListNode.print(y)
x.next = y  
s = Solution()
print(s.detectCycle(head))     
