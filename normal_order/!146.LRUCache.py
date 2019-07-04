'''

146. LRU Cache

Medium

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''

class LRUCache:

    def __init__(self, capacity: int):
        self.LRU = {}
        self.stack = []
        self.capacity = capacity
    def print(self):
        print('LRU:',self.LRU)
        print('stack:',self.stack)
    def get(self, key: int) -> int:
        try:
            val = self.LRU[key]
            index = self.stack.index(key)
            del self.stack[index]
            self.stack.append(key)
            return val
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            index = self.stack.index(key)
            del self.stack[index]
            self.stack.append(key)   
            self.LRU[key] = value         
        except:
            if len(self.stack) > self.capacity-1:
                out = self.stack.pop(0)
                del self.LRU[out]            
            self.stack.append(key)
            self.LRU[key] = value            

["LRUCache","get","put","get","put","put","get","get"]
[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
a = {}
a[3] = 3
a[1] = 1
a[2] = 2
print(a)
# obj = LRUCache(2)
# obj.put(2,1)
# obj.print() 
# obj.put(1,1)
# obj.print()
# obj.put(2,3)
# obj.print()
# obj.put(4,1)
# obj.print()
# obj.get(1)
# obj.print()
# obj.get(2)
# obj.print()