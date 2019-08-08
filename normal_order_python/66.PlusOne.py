'''
39.1%	Easy

66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.


'''


class Solution:
    from collections import deque
    def plusOne(self, digits: list) -> list:
        s = ''
        output = []
        for i in digits:
            s += str(i)
        num = int(s) + 1
        # equals to: num = int(''.join([str(i) for i in digits])) + 1
        
        while(num):
            output.insert(0, num % 10)
            num = num //10
            
        return output

