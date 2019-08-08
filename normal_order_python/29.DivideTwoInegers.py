'''

tags: Binary Search

29. Divide Two Integers

Medium

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


'''

dividend = 14
divisor = 3
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        if dividend < 0 < divisor or dividend > 0 > divisor:
            flag = -1
        else:
            flag = 1
        dividend, divisor = abs(dividend), abs(divisor)
        while(dividend >= divisor):
            tmp, val= divisor, 1
            while(dividend >= tmp):
                dividend -= tmp
                res += val
                tmp += tmp
                val += val
            
        if flag == -1:
            res = -res
        return max(min(res, 2147483647), -2147483648)

s = Solution()
print(s.divide(dividend, divisor))    