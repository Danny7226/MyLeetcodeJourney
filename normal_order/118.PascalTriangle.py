'''

118. Pascal's Triangle

Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            tmp = [1]*(i+1)
            # if i == 0:
            #     output.append(tmp)
            #     continue
            # range(1,0) or range(0,0) is a correct syntax and will not work
            for j in range(1,i):
                tmp[j] = pre[j-1] + pre [j]
            output.append(tmp)
            pre = tmp
        return output