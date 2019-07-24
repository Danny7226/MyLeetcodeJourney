'''

1095 Find in Mountain Array

Hard

(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

'''

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

mountain_arr, target = [3,5,3,2,0], 0

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        leng = mountain_arr.length()
        left, right = 0, leng-1
        # find peak
        while left < right: # there is definitely a peak, so we use '<' instead of '<='
            mid = (left+right) // 2
            if mountain_arr.get(mid) >= mountain_arr.get(mid+1):
                right = mid
            else:
                # 'left' and 'right' could be consecutive
                # 'mid' intends to be 'left', so we need 'left' to plus one to avoid endless loop
                left = mid + 1 
        peak = left
        if target == mountain_arr.get(peak):
            return peak

        # search behind the peak
        l, r = 0, peak-1
        while l <= r: # there may not be a target behind the peak, so using '<='
            print(l, r, end =' ')
            mid = (l + r) // 2
            print('1:', mid)
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            elif cur > target:
                r = mid - 1
            else:
                l = mid + 1
                
        # search after the peak
        l, r = peak+1, leng-1
        while l <= r: # there may not be a target after the peak, so using '<='
            print('2:', mid)
            mid = (l + r) // 2
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            elif cur > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

s = Solution()
print(s.findInMountainArray(target, mountain_arr))        