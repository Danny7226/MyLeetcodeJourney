'''

88. Merge Sorted Array

Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

'''

nums1, m = [1,2,3,0,0,0], 3
nums2, n = [2,5,6], 3

class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1
        ptr2 = n - 1
        while(ptr1 >= 0) and (ptr2 >= 0):
            if nums1[ptr1] < nums2[ptr2]:
                nums1[ptr1+ptr2+1] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[ptr1+ptr2+1] = nums1[ptr1]
                ptr1 -= 1
        if ptr2 >= 0:
            nums1[:ptr2+1] = nums2[:ptr2+1] 

s = Solution()
s.merge(nums1,m,nums2,n)
print(nums1)            