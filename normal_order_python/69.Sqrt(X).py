'''

tags: binary search

69. Sqrt(x)

Easy

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

'''
x = 19
class Solution:
    def mySqrt(self, x: int) -> int:
        a = int(x**0.5)
        b = round(x**0.5,2) # 保留2位小数
        return a,b
s = Solution()
print(s.mySqrt(x))

class Solution:
	# binary search
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        output = 0
        while(low <= high):
            mid = low + (high - low)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                high = mid - 1
                output = mid - 1
            else:
                low = mid + 1
                output = mid
        return output
