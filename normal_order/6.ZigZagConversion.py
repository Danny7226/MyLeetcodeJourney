'''
6. ZigZag Conversion


The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I


'''

a = "PAYPALISHIRING"

class Solution:
    def convert(s: str, numRows: int) -> str:
        K = numRows
        output = [''] * K
        index = 0
        direct = 1

        if K == 1 :
            output[0] = s
            return ''.join(output)
        for i in range(len(s)):
            output[index] += s[i]
    
            if (index == 0):
                direct = 1
            elif(index == (K-1)):
                direct = 0

            if (direct == 1):
                index += 1
            else:
                index -= 1
                
                
        print(output)
        return (''.join(output))

print(Solution.convert(a,3))