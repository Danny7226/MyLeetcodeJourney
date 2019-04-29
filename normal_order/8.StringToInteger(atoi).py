'''

8. String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

'''

s = "  -41.9-6 with words"

# class Solution:
#     def myAtoi(s: str) -> int:
#         s = s.lstrip(' ')
#         if (len(s) == 0 or s in '+-'):
#             return 0
#         if not (s.lstrip('-+')[0].isdigit()):
#         # starts with alpha
#             return 0

#         for i in range(len(s)):
#             if(s[i].isdigit() or s[i] in '.+-'):

#                 continue
#             else: 
#                 s = s[:i]
#                 break

#         print(s)
#         count = 0
#         for i in range(len(s)):
#             if (s[i].isdigit()):
#                 count = 1
#             elif(count == 1):
#             	s = s[:i]
#             	break
#         print(s)


#         if(s.count('-')+s.count('+')) > 1:
#         	return 0
#         if('-' in s.lstrip('+-') or '+' in s.lstrip('+-')):
#             return 0

#         if('.' in s):
#         	s = float(s)
#         output = int(s)
#         # print('s:', s)
#         # print('s:', float(s))

#         if output > (2**31 - 1):
#             return (2**31 - 1)
#         if output < (-(2**31)):
#             return -(2**31)
#         return output

import re

class Solution:
    def myAtoi(s: str) -> int:
        mx = 2147483647
        mi = -2147483648
        main = re.search('^[+-]?\d+', s.strip())
        # ^: from beginning
        # [+-]: only singel '+' or singel '-' will be matched
        # ?: [+-] repeated time can be 0 or 1
        # \d: digits
        # +: \d will match 1 or more times
        # *: \d will match 0 or more times
        
        if (main == None):
            return 0

        print(main.span())   
                 
        main = int(main.group(0))
        
        if main > mx:
            return mx
        if main < mi:
            return mi
        return main


print(Solution.myAtoi(s))
# print(s.strip().lstrip('-+'))
