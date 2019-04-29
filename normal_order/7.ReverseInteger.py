'''


7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21


Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.

'''


# sth[i:j:s] from i(included) to j(excluded) by step s(defaults 1)

i = 123
class Solution:
    def reverse(x: int) -> int:
        if (x >= 0):
            toStringR = reversed(str(x))
            out = int(''.join(list(toStringR)))
            # or: out = str(x)[::-1]

        else:
            toStringR = reversed(str(x).lstrip('-'))
            out = -int(''.join(list(toStringR)))
            # or: out = str(x)[1:][::-1]


        if (out > (2**31 - 1)) or (out < -(2**31)):
            return 0
        else: return out

print(Solution.reverse(i))
