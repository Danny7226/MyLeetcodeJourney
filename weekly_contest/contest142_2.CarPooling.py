'''

1094. Car Pooling

Medium

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true

'''

trips, capacity = [[9,3,4],[9,1,7],[4,2,4],[7,4,5]], 23

class Solution:
    def carPooling(self, trips: list, capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        print(trips)
        drop = []
        for i in trips:
            drop.append(([i[0],i[2]]))
            capacity -= i[0]
            if capacity < 0 :
                drop.sort(key = lambda x:x[1])
                while drop and drop[0][1]<=i[1]:
                    tmp = drop.pop(0)
                    capacity += tmp[0]
            if capacity >= 0:
                continue
            else:
                return False
        return True

s = Solution()
print(s.carPooling(trips, capacity))

