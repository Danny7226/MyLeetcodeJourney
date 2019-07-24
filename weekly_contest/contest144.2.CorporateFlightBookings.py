'''

1109. Corporate Flight Bookings

Medium

There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]

'''

bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        mark = [0] * (n+1)
        for i in bookings:
            mark[i[0]-1] += i[2]
            mark[i[1]] += -i[2]
        # print(mark)
        for i in range(1, len(ans)):
            mark[i] = mark[i] + mark[i-1]
        return mark[:-1]

s = Solution()
print(s.corpFlightBookings(bookings,n))        
