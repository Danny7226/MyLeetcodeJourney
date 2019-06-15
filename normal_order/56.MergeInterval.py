'''

56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''

intervals = [[1,3],[2,6],[8,10],[15,18]]

class Solution:
    def merge(self, intervals: list) -> list:
        if len(intervals) < 1:
            return []    
        intervals.sort(key = lambda x:x[0], reverse = False) 
        # key = lambda x:x[] is a standard syntax
        # means sort by specific element

        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            print(ans)
            if intervals[i][0]<= ans[-1][1]:
                ans[-1] = [ ans[-1][0], max(intervals[i][1], ans[-1][1]) ]
            else:
                ans.append(intervals[i])
        return ans
s = Solution()
print(s.merge(intervals))        