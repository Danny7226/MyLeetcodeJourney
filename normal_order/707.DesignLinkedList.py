'''

707. Design Linked List

Easy

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3


'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
        
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.LL = []


    def print(self):
        val = []
        for i in self.LL:
            val.append(i.val)
        print(val)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0 <= index < len(self.LL):
            return self.LL[index].val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        
        new = ListNode(val)
        if self.LL:
            new.next = self.LL[0]
        self.LL.insert(0,new)
        
        return self.LL[0]

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new = ListNode(val)
        if self.LL:
            self.LL[-1].next = new
        self.LL.append(new)
        return self.LL[0]
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new = ListNode(val)
        if not self.LL:
            if index == 0 or index == -1:
                self.LL.append(new)
                return self.LL[0]
            else:
                return
        else:
            if index == 0:
                new.next = self.LL[0]
                self.LL.insert(0,new)
                return self.LL[0]
            elif index > len(self.LL):
                return self.LL[0]
            elif index == len(self.LL):
                self.LL[-1].next = new
                self.LL.append(new)
            else:
                pre = self.LL[index-1]
                pre.next, new.next = new, self.LL[index]
                self.LL.insert(index,new)
                return self.LL[0]

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if 0 < index < len(self.LL):
            if index != len(self.LL)-1:
                self.LL[index-1].next = self.LL[index+1]
            else:
                self.LL[index-1].next = None
            del self.LL[index]
            return self.LL[0]
        elif index == 0:
            self.LL.pop(0)
            if self.LL:
                return self.LL[0]
            else:
                return
        else:
            if self.LL:
                return self.LL[0]
            else:
                return
            

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
# obj.print()
print(obj.get(1))
obj.deleteAtIndex(1)
obj.get(1)
# obj.print()
# obj.deleteAtIndex(index)