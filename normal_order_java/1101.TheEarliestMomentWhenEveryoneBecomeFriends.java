class UnionFind{
    private int[] union;
    public UnionFind(int size){
        this.union = new int[size];
        for(int i = 0; i < size; i++){
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
class Solution {
    class CustomCompare implements Comparator<int[]>{
        public int compare(int[] a, int[] b){
            return a[0] - b[0];
        }
    }
    public int earliestAcq(int[][] logs, int N) {
        UnionFind uf = new UnionFind(N);
        Arrays.sort(logs, new CustomCompare());
        for(int[] relation: logs){
            uf.unite(relation[1],relation[2]);
            if(check(uf, N)) return relation[0];
        }
        
        return -1;
    }
    
    public boolean check(UnionFind uf, int N){
        int cur;
        int criteria = uf.find(0);
        for(int i = 1; i < N; i++){
            cur = uf.find(i);
            if(cur != criteria) return false;
        }
        return true;
    }
}