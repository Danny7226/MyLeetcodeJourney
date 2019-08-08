'''
923. 3Sum With Multiplicity
Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
As the answer can be very large, return it modulo 10^9 + 7.
Example 1:
Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:
Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
Note:
3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
'''
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        count = [0] * 101
        ans = 0
        for n in A:
            count[n] += 1
        for x in range(101):
            for y in range(x+1,101):
                z = target - x - y
                if x<y<z<=100:
                    ans += count[x] * count[y] * count[z]
                    ans %= 10**9 + 7
                    
        for x in range(101):
            z = target - 2*x
            if 0<=z<=100 and x!=z:
                ans += count[x]*(count[x]-1)//2*count[z]
                ans %= 10**9 + 7
                
        if not target % 3:
            x = target//3
            if 0<=x<=100:
                ans += count[x] * (count[x]-1) * (count[x]-2)//6
                ans %= 10**9 + 7
        return ans
