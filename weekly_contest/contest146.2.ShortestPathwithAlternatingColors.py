'''
5132. Shortest Path with Alternating Colors
Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.
Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.
Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).
Example 1:
Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:
Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:
Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
Example 4:
Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
Example 5:
Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph, queue, ans = collections.defaultdict(list), collections.deque(), [-1] * n
        red, blue = 1, 2
        seen, done = set(), set()
        for i, j in red_edges:
            graph[i].append((j, red))
        for a, b in blue_edges:
            graph[a].append((b, blue))
        # print(graph)    
        ans[0] = 0
        done.add(0)
        for edge in graph[0]:
            queue.append((edge, None, 0))
            seen.add(edge)
        while queue:
            (node, color), color_prev, count = queue.popleft()
            # print(node, color, color_prev, seen)
            if color == color_prev:
                continue
            count += 1
            seen.add((node, color))
            if node not in done:
                done.add(node)
                ans[node] = count
            for edge in graph[node]:
                if edge not in seen:
                    # print(edge[0])
                    queue.append((edge, color, count))                     
        return ans