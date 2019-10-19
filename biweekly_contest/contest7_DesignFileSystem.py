class ListNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = {}
    
class FileSystem(object):

    def __init__(self):
        self.cache = ListNode(None, None)

    def create(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        steps = path.split('/')[1:]
        cur = self.cache
        for i in range(len(steps)-1):
            # print(steps[i], cur.next)
            if steps[i] not in cur.next:
                return False
            else:
                cur = cur.next[steps[i]]
        cur.next[steps[-1]] = ListNode(steps[-1], value)
        return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        steps = path.split('/')[1:]
        cur = self.cache
        for i in range(len(steps)-1):
            if steps[i] not in cur.next:
                return -1
            else:
                cur = cur.next[steps[i]]
        return cur.next[steps[-1]].val if steps[-1] in cur.next else -1;
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)