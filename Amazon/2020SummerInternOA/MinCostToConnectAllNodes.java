// Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

// Input:

// n, an int representing the total number of nodes.
// edges, a list of integer pair representing the nodes already connected by an edge.
// newEdges, a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, respectively (e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).
// Example 1:

// Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
// Output: 7
// Explanation:
// There are 3 connected components [1, 4, 5], [2, 3] and [6].
// We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.
// Solution
// Related problems:

// Min Cost to Repair Edges
// https://leetcode.com/problems/connecting-cities-with-minimum-cost (premium)
import java.util.*;

public class MinCostToConnectAllNodes{
    public static void main(String[] args){
        Solutions s = new Solutions();
        System.out.println(s.getAnswer(6, new int[][]{{1,4}, {4,5}, {2,3}}, new int[][]{{1,2,5}, {1,3,10}, {1,6,2}, {5,6,5}}));
    }
}

class Solutions{
    class CustComp implements Comparator<int[]>{
        public int compare(int[] a, int[] b){
            return a[2] - b[2];
        }
    }
    public int getAnswer(int n, int[][] edges, int[][] newEdges){
        int ans = 0;
        UnionFind uf = new UnionFind(n);
        for(int[] edge: edges) uf.unite(edge[0], edge[1]);
        Arrays.sort(newEdges, new CustComp());
        for(int[] e: newEdges){
            if(uf.find(e[0]) == uf.find(e[1])) continue;
            // System.out.println(e[0] + " " + e[1]);
            ans += e[2];
            uf.unite(e[0], e[1]);
        }
        if(uf.checkAllConnected()) return ans;
        else return -1;
    }
}

class UnionFind{
    int[] union;
    public UnionFind(int k) {
        union = new int[k+1];
        for(int i = 0; i < k+1; i++) union[i] = i;
    }
    public int find(int x){
        if(union[x] != x) union[x] = find(union[x]);
        return union[x];
    }
    public void unite(int x, int y){
        if(find(x) < find(y)) union[find(y)] = find(x);
        else union[find(x)] = find(y);
    }
    public boolean checkAllConnected(){
        Set<Integer> set = new HashSet<>();
        for(int i = 1; i < union.length; i++) {set.add(find(i));}
        return set.size() == 1;
    }
}