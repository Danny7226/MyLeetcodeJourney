'''
tags: BFS
815. Bus Routes
Hard

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.
We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.
Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Note:
1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.
'''
class Solution:
    # least bus taken, so BFS
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        bus_instop, queue = collections.defaultdict(set), collections.deque()
        ans = -1
        for bus, route in enumerate(routes):
            for s in route:
                bus_instop[s].add(bus)
        # print(bus_instop)
        seen = set()
        for bus in bus_instop[S]:
            queue.append((routes[bus], 1))
            seen.add(bus)
        while queue:
            stops, taken = queue.popleft()
            # print(stops, taken)
            for stop in stops:
                if stop == T:
                    return taken
                else:
                    for nxt_bus in bus_instop[stop]:
                        if nxt_bus not in seen:
                            seen.add(nxt_bus)
                            queue.append((routes[nxt_bus], taken+1))
        return ans
        