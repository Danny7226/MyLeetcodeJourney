'''

802. Find Eventual Safe States
Medium

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.
Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.
Which nodes are eventually safe?  Return them as an array in sorted order.
The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.
Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Note:
graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].
'''

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.processing, self.done = 1, 2
        self.processed = [0] * len(graph)
        self.ans, self.incycle = [], [False] * len(graph)
        self.children = collections.defaultdict(list)
        for i, edgs in enumerate(graph): # O(N) average
            for j in edgs:
                self.children[i].append(j)
        for i in range(len(graph)):
            if self.processed[i] == 0:
                self.dfs(i)
        return sorted(self.ans)
    
    def dfs(self, i, father = None):
        # print(i)
        self.processed[i] = self.processing
        for child in self.children[i]:
            if self.processed[child] == self.done:
                continue
            if self.processed[child] == self. processing:
                return False
            else:
                if not self.dfs(child, i):
                    self.incycle[i] = True
                    return False
        self.processed[i] = self.done
        if not self.incycle[i]:
            self.ans.append(i)
        return True
        