'''

119.PascalTriangleII.py

Easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        output_pre = self.getRow(rowIndex-1)
        output = [1] * (rowIndex+1)
        for i in range(1, len(output)-1):
            output[i] = output_pre[i-1] + output_pre[i]
        return output

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = []
        for i in range(rowIndex+1):
            tmp = [1]*(i+1)
            for j in range(1,i):
                tmp[j] = pre[j-1] + pre [j]
            output.append(tmp)
            pre = tmp
        return output[-1] 