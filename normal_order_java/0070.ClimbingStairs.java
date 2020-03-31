class Solution {
    static List<Integer> ans = new ArrayList<>();
    public int climbStairs(int n) {
        if(ans.size() > n) return ans.get(n);
        if(ans.size() == 0) ans.add(1);
        if(ans.size() == 1) ans.add(1);
        if(ans.size() == 2) ans.add(2);
        for(int i = ans.size(); i <= n; i++){
            ans.add(ans.get(i-1) + ans.get(i-2));
        }
        return ans.get(n);
    }
}

class Solution {
    static int[] ans = new int[99999];
    int index = 0;
    public int climbStairs(int n) {
        if(index > n) return ans[n];
        if(index == 0) ans[index++] = 0;
        if(index == 1) ans[index++] = 1;
        if(index == 2) ans[index++] = 2;
        while(index <=n){
            ans[index] = ans[index-1] + ans[index++-2];
        }
        return ans[n];
    }
}