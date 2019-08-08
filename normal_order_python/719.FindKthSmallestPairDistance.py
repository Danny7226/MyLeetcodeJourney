'''
719. Find K-th Smallest Pair Distance
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.
Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        def helper(mid):
            count = left = 0
            for i in range(len(nums)):
                while nums[i] - nums[left] > mid:
                    left += 1
                count += i - left
                # if count > k:
                #     break
            return count >= k
        while lo < hi:
            mid = (lo + hi)//2
            if helper(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
            