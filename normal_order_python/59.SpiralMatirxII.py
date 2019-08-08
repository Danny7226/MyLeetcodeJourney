'''

59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''
n = 4

class Solution:
    def generateMatrix(self, n: int) -> list:
        ans = [[False]* n for _ in range(n)]
        r, c, di = 0, 0, 0
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        for i in range(1, n**2+1):
            ans[r][c] = i
            nr, nc = r + dr[di], c + dc[di]
            if 0<=nr<n and 0<=nc<n and not ans[nr][nc]:
                r, c = nr, nc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans

s = Solution()
ans = s.generateMatrix(n)
for i in ans:
	print(i)