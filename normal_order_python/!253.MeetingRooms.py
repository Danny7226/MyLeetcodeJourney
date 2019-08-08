x = [7, -8, 5, 4, 0, -2, -5]
x.sort(key = lambda x:(x<0,abs(x)))
print(x)

intervals = [[0,30],[5,10],[15,20]]
class Solution:
    # O(NlogN)
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])
        ans = 1
        for i in range(1, len(intervals)):
            cur_start, prev_end = intervals[i][0], intervals[i-1][1]
            if cur_start < prev_end:
                ans += 1
        return ans

class Solution:
    def minMeetingRooms(self, intervals):
        if intervals is None or len(intervals) == 0:
            return 0
        tmp = []
        # mark starting points and ending points
        for inter in intervals:
            tmp.append((inter[0], True))
            tmp.append((inter[1], False))

        # sort
        tmp = sorted(tmp, key=lambda v: (v[0], v[1]))
        n = 0
        max_num = 0
        for arr in tmp:
            # meet starting points +1
            if arr[1]:
                n += 1
            # meet ending points -1
            else:
                n -= 1
            max_num = max(n, max_num)
        return max_num
s = Solution()        
print(s.minMeetingRooms(intervals))