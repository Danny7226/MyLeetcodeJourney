'''

136. Single Number

Easy 

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

'''

class Solution:
    # with extra memory
    def singleNumber(self, nums: list) -> int:
        check = {}
        for i in nums:
            if i not in check:
                check[i] = 1
            else:
                check[i] += 1
        for i in check:
            if check[i] == 1:
                return i

class Solution(object):
    # dict pop() method
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

class Solution:
    # bit manipulation
    def singleNumber(self, nums: list) -> int:
        a = 0
        for i in nums:
            a = a ^ i
        return a     

class Solution:
    # math
    def singleNumber(self, nums: List[int]) -> int:
        a = sum(set(nums)) * 2 - sum(nums)
        return a           

a = {1:1, 2:2}
a.popitem()[1]
print(a)
a = {1:1, 2:2}
a.pop(1)
print(a)