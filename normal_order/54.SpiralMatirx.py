'''

54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

class Solution:
    def spiralOrder(self, matrix: list) -> list:
        if not matrix:
            return []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in range(R)]
        ans = [0]*(R*C)
        # print(seen)
        r, c, di = 0, 0, 0
        for i in range(R*C):
            print(r,c)
            ans[i] = matrix[r][c]
            seen[r][c] = True
            nr, nc = r + dr[di], c + dc[di] # 'nr, nc' means 'next_r, next_c'
            # print(nr,nc)
            if 0<=nr<R and 0<=nc<C and not seen[nr][nc]:
                r, c = nr, nc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
        
# class Solution:
#     def spiralOrder(self, matrix: list) -> list:
#         if not matrix:
#             return []
#         i, j, imax, jmax = 0, 0, len(matrix), len(matrix[0])
#         leng = imax * jmax
#         res = [0] * leng
#         imin, jmin = 1, 0
#         index = 0
#         while index < leng:
#             while index < leng and j < jmax:
#                 res[index] = matrix[i][j]
#                 j += 1
#                 index += 1
#             print('1',index,res)
#             jmax -= 1
#             j -= 1
#             i += 1
#             while index < leng and i < imax:
#                 res[index] = matrix[i][j]
#                 i += 1
#                 index += 1
#             print('2',index,res)
#             imax -= 1
#             i -= 1
#             j -= 1
#             while index < leng and j >= jmin:
#                 res[index] = matrix[i][j]
#                 j -= 1
#                 index += 1
#             print('3',index,res)
#             jmin += 1
#             j += 1
#             i -=1
#             while index < leng and i >= imin:
#                 res[index] = matrix[i][j]
#                 i -= 1
#                 index += 1
#             print('4',index,res)
#             imin += 1
#             i += 1
#             j += 1
#         return res
s = Solution()
print(s.spiralOrder(matrix))        