arr1, arr2 = [0], [1,1,1,1,1]

class Solution:
    def addNegabinary(self, arr1: list, arr2: list) -> list:
        n1 = self.getNumber(arr1)
        n2 = self.getNumber(arr2)
        n = n1 + n2
        return self.getList(n)
        
    def getNumber(self, arr):
        res = 0
        counter = 0
        while arr:
            res += arr.pop() * ((-2) ** counter)
            counter += 1
        return res
        
    def getList(self, n):
        if n == 0:
            return [0]
        ans = []
        while(n):
            reminder = abs(n % (-2))
            print(n, reminder)
            ans.insert(0, reminder)
            n = (n - reminder) // (-2)
        return ans

s = Solution()
print(s.addNegabinary(arr1,arr2)) 