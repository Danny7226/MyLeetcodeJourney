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


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hash_table = {}
        n = 0        
        while head:
            if head in hash_table:
                return head
            else:
                hash_table[head] = n
                n += 1
                head = head.next
        return None

class Solution:
    # @param head, a ListNode
    # @return a list node

    # If fast and slow both start at head, when fast catches slow, slow has traveled H+D and fast 2(H+D). 
    # Assume fast has traveled n loops in the cycle, we have:
    # 2H + 2D = H + D + nL  -->  H + D = nL  --> H = nL - D    
    def detectCycle(self, head):
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            # if there is an exception, we reach the end and there is no cycle
            return None

        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head        

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
