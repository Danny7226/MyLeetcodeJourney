'''

tags: bin math

67. Add Binary

Easy

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''

a = '0'
b = '0'
class Solution:
    def addBinary(self, a:str, b:str) -> str:
        a = int(a, base = 2)
        b = int(b, base = 2)
        sum = a + b
        # print(type(a))
        # int(a, 2) returns <class 'int'>v
        return bin(sum)[2:]
        # bin() returns a binary string!!!!
        # bin(sum) returns <class 'str'>

s = Solution()
print(s.addBinary(a,b))        

# int() cannot convert non-string
# x = 11
# print(int(x, base = 2))
