'''
826. Most Profit Assigning Work
We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 
Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 
Every worker can be assigned at most one job, but one job can be completed multiple times.
For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.
What is the most profit we can make?
Example 1:
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
Notes:
1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
'''
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        for i in range(len(difficulty)):
            difficulty[i] = (difficulty[i], profit[i])
        difficulty.sort(key = lambda x:x[0]) # O(NlogN)
        i, L = 0, len(difficulty)
        ans, most = 0, 0
        for wker in sorted(worker):
            while i < L and difficulty[i][0] <= wker:
                most = max(most, difficulty[i][1])
                i += 1
            ans += most
        return ans

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job = sorted(zip(difficulty, profit))
        i, L = 0, len(job)
        ans, most = 0, 0
        for wker in sorted(worker):
            while i < L and job[i][0] <= wker:
                most = max(most, job[i][1])
                i += 1
            ans += most
        return ans        
            