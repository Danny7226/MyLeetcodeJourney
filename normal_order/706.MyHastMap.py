'''

706. Design HashMap

Easy

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

'''
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.volumn = 2000
        self.cache = [None] * self.volumn
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        pseudo = key % self.volumn
        cur = self.cache[pseudo]
        if cur:
            while True:
                if cur.key == key:
                    cur.val= value
                    return
                elif cur.next == None:
                    cur.next = ListNode(key,value)
                    break
                else:
                    cur = cur.next
            
        else:
            self.cache[pseudo] = ListNode(key,value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        pseudo = key % self.volumn
        cur = self.cache[pseudo]
        if cur:
            while cur:
                if cur.key == key:
                    return cur.val
                else:
                    cur = cur.next
        return -1

        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        pseudo = key % self.volumn
        cur = self.cache[pseudo]
        if cur:
            dummy = ListNode(None,None)
            dummy.next = cur
            ans = dummy
            while cur:
                if cur.key == key:
                    dummy.next = cur.next
                    self.cache[pseudo] = ans.next
                    break
                else:
                    dummy, cur = cur, cur.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)