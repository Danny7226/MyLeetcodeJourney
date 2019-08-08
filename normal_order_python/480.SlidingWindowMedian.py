'''

tags: prior queue (heap)

480. Sliding Window Median

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.

'''
class Solution:
    def medianSlidingWindow(self, nums, k):
        low, high = [], [] # heap
        for i in range(k):
            heapq.heappush(high, (nums[i], i)) # high is a min-heap
        for _ in range(k>>1):
            self.convert(high, low)
        ans = [high[0][0]*1. if k&1 else (high[0][0]-low[0][0])/2.]
        for i in range(len(nums[k:])):
            if nums[i+k] >= high[0][0]:
                heapq.heappush(high, (nums[i+k], i+k))
                if nums[i] <= high[0][0]: # keep the number of elements between two heap always in balance
                    self.convert(high, low)
            else:
                heapq.heappush(low, (-nums[i+k], i+k))
                if nums[i] >= high[0][0]:
                    self.convert(low, high)
            while low and low[0][1] <= i: heapq.heappop(low)
            while high and high[0][1] <= i: heapq.heappop(high)
            ans.append(high[0][0]*1. if k&1 else (high[0][0]-low[0][0])/2.)
        return ans
        
                    
    def convert(self, heap1, heap2): # convert min-heap1 to max-heap2
        element, index = heapq.heappop(heap1)
        heapq.heappush(heap2, (-element, index))