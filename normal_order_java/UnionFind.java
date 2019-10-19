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

class UnionFind{
    Map<Character, Character> union = new HashMap<>();
    UnionFind(){
        for(char i = 'a'; i <='z'; i++){
            union.putIfAbsent(i, i);
        }
    }
    public char find(char x){
        if(union.get(x) != x) union.put(x, find(union.get(x)));
        return union.get(x);
    }
    public void unite(char x, char y){
        char fx = find(union.get(x));
        char fy = find(union.get(y));
        if(fx > fy){ // lexicographical order priority
            char temp = fx;
            fx = y;
            fy = temp;
        }
        union.put(fy, fx);
    }
}