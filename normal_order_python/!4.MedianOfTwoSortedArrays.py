'''

tag: binary search

4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''

class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     num = sorted(nums1 + nums2)
    #     leng = len(num)
    #     median = 0
    #     if ( (leng%2) == 1):
    #         median = num[(leng-1)//2]
    #     else:
    #         median = (num[leng//2] + num[leng//2 - 1]) / 2
    #     return median


 	
	def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:

        """
        60ms, faster than 97.02%
        """
        
        # Ensure nums1 is longer than nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        # Get lengths and starting binary search min & max
        m = len(nums1)
        n = len(nums2)
        imin = 0
        imax = m
        half_len = (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
            # i is too small, must increase it
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
                continue
            
            # i is too big, must decrease it
            if i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
                continue
            
            # i is perfect, we can find our median's position!
            # Find the max of the left partition
            if i == 0:
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])
            
            # If even length, the median is simply the max of the left partition
            if (m + n) % 2 == 1:
                return max_of_left
            
            # Otherwise, we also need the min or tthe right partition
            # Find min of the right partition
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            
            return (max_of_left + min_of_right) / 2.0

    '''

 	'''