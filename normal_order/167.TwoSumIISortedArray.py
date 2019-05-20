'''

167. Two Sum II - Input array is sorted

Easy

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

'''


class Solution(object):
	# 2 ptrs
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ptr1 = 0
        ptr2 = len(numbers) - 1
        while ptr1 < ptr2:
            while numbers[ptr1] + numbers[ptr2] > target:
                ptr2 -= 1
            if numbers[ptr1] + numbers[ptr2] == target:
                return [ptr1+1, ptr2+1]
            ptr1 += 1

        return None

class Solution(object):
	# hash_table (dictionary)
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(numbers)):
            if numbers[i] in hash_table:
                return [hash_table[numbers[i]], i+1]
            else:
                hash_table[target - numbers[i]] = i + 1
        return None        