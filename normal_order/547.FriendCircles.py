'''

tags: DFS, Union Find

547. Friend Circles

Medium

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.

'''
import collections
M = [
[1,0,0,1],
[0,1,1,0],
[0,1,1,1],
[1,0,1,1]]

class Solution:
    # union find
    def findCircleNum(self, M: list) -> int:
        n = len(M)
        union = [i for i in range(n)]

        def find(x):
            if union[x] != x:
                union[x] = find(union[x])
            return union[x]

        def unite(x, y):
            union[find(y)] = find(x)
            
        # # attach a lower-rank parent to the higher-rank one
        # def union(x, y):
        #     px, py = find(x), find(y)
        #     if rank[px] < rank[py]: px, py = py, px  
        #     p[py] = px
        #     rank[px] += 1            
            
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j]:
                    unite(i,j)
                    
        # for i in range(n):
        #     union[i] = find(i)
        print(union)
        return len(set(map(find,union)))
        
# class Solution:
#     # DFS & BFS
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         friend = collections.defaultdict(set)
#         seen, circles, n =set(), [], len(M)
#         for i in range(n): # O(N^2)
#             for j in range(i+1, n):
#                 if M[i][j]:
#                     friend[i].add(j)
#                     friend[j].add(i)
#         print(friend)

#         def dfs(person, circle): # you can also call it backtrack
#             nonlocal seen
#             seen.add(person)
#             circle.add(person)
#             for j in friend[person]:
#                 if j not in seen:
#                     dfs(j, circle)
#             return circle
        
#         for person in range(n): # O(N)
#             if person not in seen:
#                 circles.append( dfs(person,set()) )
#         print(circles)
#         return len(circles)
        
#         # def BFS(queue, circle):
#         #     seen.add(queue[0])
#         #     for person in queue:
#         #         circle.add(person)
#         #         for j in friend[person]:
#         #             if j not in seen:
#         #                 seen.add(j)
#         #                 queue.append(j) # Python list append is time consuming, so recursion DFS is better in time.
#         #     return circle
        
#         # for person in range(n):
#         #     if person not in seen:
#         #         circles.append(BFS([person],set()))
#         # print(circles)        
#         # return len(circles)

s = Solution()
print(s.findCircleNum(M))        












