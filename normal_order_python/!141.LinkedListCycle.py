'''


'''
linked_list = [3,2,0,4]
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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        hash_table = []
        while head:
            if head in hash_table:
                return True
            hash_table.append(head)
            head = head.next
        return False

class Solution(object):
    # hash_table this one is the fastest
    # set() is faster than dict faster than list when doing searching
    def hasCycle(self, head):
        hash_table = set()
        while head:
            if head in hash_table:
                return True
            hash_table.add(head)
            head = head.next
        return False

class Solution(object):
    # !!!2 ptrs
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        ptr1 = head
        ptr2 = head.next
        while(ptr1 != ptr2):
            try:
                ptr1 = ptr1.next
                ptr2 = ptr2.next.next
            except:
                return False
        return True

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
print(s.hasCycle(head))