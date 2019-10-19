class UnionFind{
    private int[] union;
    UnionFind(int size){
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

class Comp implements Comparator<int[]>{
    public int compare(int[] a, int[] b){
        return a[2] - b[2];
    }
}
class Solution {
    public int minimumCost(int N, int[][] connections) {
        UnionFind uf = new UnionFind(N);
        Arrays.sort(connections, new Comp());
        int ans = 0;
        for(int i = 0; i < connections.length; i++){
            int[] cur = connections[i];
            if(uf.find(cur[0]) != uf.find(cur[1])){
                uf.unite(cur[0], cur[1]);
                ans += cur[2];
                N--;
            }
            if(N==1) return ans;
        }
        return -1;
    }
}