class UnionFind{
    HashMap<Character, Character> union;
    UnionFind(){
        union = new HashMap<Character, Character>();
    }
    public char find(char x){
        if(union.get(x) != x) union.put(x, find(union.get(x)));
        return union.get(x);
    }
    public void unite(char x, char y){
        union.put(union.get(find(x)), union.get(find(y)));
    }
    
}

class Solution {
    public boolean equationsPossible(String[] equations) {
        String cur;
        UnionFind uf = new UnionFind();
        for(int i = 0; i < equations.length; i++){
            cur = equations[i];
            uf.union.putIfAbsent(cur.charAt(0), cur.charAt(0));
            uf.union.putIfAbsent(cur.charAt(3), cur.charAt(3));
            if(cur.charAt(1) == '='){
                uf.unite(cur.charAt(0), cur.charAt(3));
            }
        }
        
        for(int i = 0; i < equations.length; i++){
            cur = equations[i];
            if(cur.charAt(1) == '!'){
                if(uf.find(cur.charAt(0)) == uf.find(cur.charAt(3))) return false;
            }
        }
        return true;
    }
}