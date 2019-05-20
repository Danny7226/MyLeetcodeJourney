'''

171. Excel Sheet Column Number

Easy

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        # print(ord('A') - 64) # 1
        # print(chr(97))  # 'a'
        output = 0
        for i in range(1, len(s)+1):
            output += (ord(s[-i]) - ord('A') + 1) * (26 ** (i-1))
        return output