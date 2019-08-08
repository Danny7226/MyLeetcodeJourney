'''

240. Search a 2D Matrix II

Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

'''

class Solution:   
	# O(m+n) 
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row, column = 0, len(matrix[0])-1
        while row<len(matrix) and column>=0:
            cur = matrix[row][column]
            if cur == target:
                return True
            elif cur > target:
                column -= 1
            else:
                row += 1
        return False

class Solution: 
	# O(m*lgn)   
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ans = False
        for row in matrix:
            print(row)
            if not row or row[0] > target or ans == True:
                return ans
            ans = self.targetInRow(row, target)
        return ans
    
    def targetInRow(self, row, target):
        left, right = 0, len(row)-1
        while left <= right:
            mid = (left + right) // 2
            cur = row[mid]
            print(cur, end = ' ')
            if cur == target:
                return True
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        