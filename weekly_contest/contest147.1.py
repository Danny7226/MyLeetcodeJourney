1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:
Input: n = 25
Output: 1389537

class Solution:
    sequence = [0,1,1]
    def tribonacci(self, n: int) -> int:
        while n > len(self.sequence)-1:
            self.sequence.append(self.sequence[-1]+self.sequence[-2]+self.sequence[-3])
        return self.sequence[n]