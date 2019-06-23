'''

tags: Binary Search

74. Search a 2D Matrix

Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

'''
matrix, target = [[1],[2],[3]], 3

class Solution(object):
def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m = len(matrix)
    n = len(matrix[0])
    
    xl = 0
    xr = m*n-1
    
    while (True):
        xm = (xl+xr)/2
        if (matrix[xm/n][xm%n] == target):
            return True
        if (xl >= xr):
            return False
        if (matrix[xm/n][xm%n] > target):
            xr = xm-1
        else:
            xl = xm+1
            
class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix[0]), len(matrix)
        l, r = 0, n
        while l < r-1:
            mid = (l+r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid
            else:
                r = mid
        row = l
        l, r = 0, m-1
        print(row)
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
s = Solution()
print(s.searchMatrix(matrix, target))        