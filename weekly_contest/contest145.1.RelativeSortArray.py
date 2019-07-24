'''

1122. Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

'''
import random
arr1, arr2 = [26,21,11,20,50,34,1,18], [21,11,26,20]

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        Map = { ele:ind for ind, ele in enumerate(arr2)}
        arr1.sort(key = lambda x:Map.get(x, 1000+x))
        return arr1

class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        dic, other = {}, []
        for i in arr2: #(m)
            dic[i] = []
        for i in arr1: #(n)
            if i in dic:
                dic[i].append(i)
            else:
                other.append(i)
        res = []
        for i in arr2: # O(m)
            res += dic[i]
        return res + self.sort(other)
        
    def sort(self, arr): # O(nlogn)
        if len(arr) <= 1:
            return arr
        pivot = random.choice(arr)
        print(pivot)
        return self.sort([i for i in arr if i < pivot]) + [i for i in arr if i == pivot] + self.sort([i for i in arr if i > pivot])

s = Solution()
print(s.relativeSortArray(arr1,arr2))        