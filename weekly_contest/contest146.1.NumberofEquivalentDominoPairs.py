'''
5130. Number of Equivalent Domino Pairs
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Constraints:
1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        s = {}
        ans = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            if (a,b) in s:   
                s[(a,b)] += 1
            else:
                s[(a,b)] = 1
        print(s)
        for key in s:
            if s[key] > 1:
                ans += self.helper(s[key])
        return ans
    
    def helper(self, x):
        return x * (x-1) // 2