'''

912. Sort an Array

Medium

Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Note:

1 <= A.length <= 10000
-50000 <= A[i] <= 50000

'''

nums = [5,1,1,2,0,0]

class Solution:
    # quick sort
    def qsort(nums):
        if not nums: return []
        p = random.choice(nums)
        return qsort([x for x in nums if x < p]) + [x for x in nums if x == p] + qsort([x for x in nums if x > p])

class Solution:
    # merge sort
    def msort(nums):
        def merge(A, B):
            C = []
            while A and B:
                C.append(A.pop(0)) if A[0] < B[0] else C.append(B.pop(0))
            return C + (A or B)
        n = len(nums)
        return nums if n < 2 else merge(msort(nums[:n>>1]), msort(nums[n>>1:]))


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Quick Sort Recursion
        if len(nums) == 1:
            return nums
        if not nums:
            return []
        pick = random.choice(nums)
        left, mid, right = [], [], []
        for i in nums:
            if i < pick:
                left.append(i)
            elif i > pick:
                right.append(i)
            else:
                mid.append(i)
        return self.sortArray(left) + mid + self.sortArray(right)

class Solution:
    # merge sort
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge Sort Recursion
        leng = len(nums)
        if leng == 1:
            return nums
        left, right = self.sortArray(nums[:leng//2]), self.sortArray(nums[leng//2:])
        return self.Merge(left, right)
    
    def Merge(self, left, right):
        l, r = 0, 0 
        ans = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ans.append(left[l])
                l += 1
            else:
                ans.append(right[r])
                r += 1
        if l == len(left):
            ans += right[r:]
        else:
            ans += left[l:]
        return ans  