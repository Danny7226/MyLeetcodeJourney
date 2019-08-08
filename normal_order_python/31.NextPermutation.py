'''

31. Next Permutation

Medium

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1



'''
import bisect
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,-1,-1):
            if i == 0:
                self.reverse(nums, i, len(nums)-1)
            if nums[i] > nums[i-1]:
                self.reverse(nums, i, len(nums)-1)
                j = bisect.bisect(nums, nums[i-1], i)
                nums[i-1], nums[j] = nums[j], nums[i-1]
                break
                
    def reverse(self, nums, p, q):
        l, r = p, q
        while l<=r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

a = [4,5,3,2,1]
j = bisect.bisect(a,4,1)
print(j)

                    