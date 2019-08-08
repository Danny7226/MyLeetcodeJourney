'''

973. K Closest Points to Origin

Medium

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

'''

class Solution:
    # quick select
    def __init__(self):
        self.ans = []
    def kClosest(self, points, K):
        l, m, r = [], [], []
        pivot = random.choice(points)
        pivot = pivot[0]*pivot[0] + pivot[1]*pivot[1]
        for i in points:
            dis = i[0]*i[0]+i[1]*i[1]
            if dis == pivot:
                m.append(i)
            elif dis > pivot:
                r.append(i)
            else:
                l.append(i)
        ll, lm, lr = len(l), len(m), len(r)
        if ll < K <= ll+lm:
            self.ans += l+m
        elif ll >= K:
            self.kClosest(l, K)
        else:
            self.ans += l+m
            self.kClosest(r, K-ll-lm)
        return self.ans

class Solution:
    # min-heap
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis = [ (e[0]**2 + e[1]**2, pos) for pos, e in enumerate(points)]
        print(dis)
        ans = []
        heapq.heapify(dis)
        for i in range(K):
            d, ind = heapq.heappop(dis)
            ans.append(points[ind])
        return ans