// There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.
// For each house i, we can either build a well inside it directly with cost wells[i], or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[i] = [house1, house2, cost] represents the cost to connect house1 and house2 together using a pipe. Connections are bidirectional.
// Find the minimum total cost to supply water to all houses.
// Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
// Output: 3
// Explanation: 
// The image shows the costs of connecting houses using pipes.
// The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
import java.util.*;
class UF{
    private int[] union;
    public UF(int size){
        this.union = new int[size+1];
        for(int i = 0; i < size+1; i++){
            union[i] = i;
        }
    }
    public int find(int x){
        if(union[x] != x) union[x] = find(union[x]);
        return union[x];
    }
    public void unite(int x, int y){
        union[find(x)] = find(y);
        return;
    }
    
}

class Triplet implements Comparable<Triplet>{
    int cost, v1, v2;
    public Triplet(int cost, int v1, int v2){
        this.cost = cost;
        this.v1 = v1;
        this.v2 = v2;
    }
    public int compareTo(Triplet that){
        return this.cost - that.cost;
    }
}

class Solution {
    public int minCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        UF uf = new UF(n);
        List<Triplet> candi = new ArrayList<>();
        int ans = 0;
        for(int i = 0; i < wells.length; i++){
            candi.add(new Triplet(wells[i], 0, i+1));
        }
        for(int i = 0; i < pipes.length; i++){
            candi.add(new Triplet(pipes[i][2], pipes[i][0], pipes[i][1]));
        }
        Collections.sort(candi);
        Triplet cur;
        for(int i = 0; i < candi.size(); i++){
            cur = candi.get(i);
            System.out.println(cur.v1 + " " + cur.v2);
            if(uf.find(cur.v1) != uf.find(cur.v2)){
                uf.unite(cur.v1, cur.v2);
                ans += cur.cost;
            }
        }
        return ans;
    }
}

public class well{
    public static void main(String[] args){
        int n = 3;
        int[] wells = {1,2,2};
        int[][] pipes = {{1,2,1},{2,3,1}};
        Solution s = new Solution();
        System.out.println(s.minCostToSupplyWater(n, wells, pipes));

    }
}