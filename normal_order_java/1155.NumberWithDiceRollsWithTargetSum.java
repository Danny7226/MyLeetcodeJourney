class Solution {
    public int numRollsToTarget(int d, int f, int target) {
        int[][] ans = new int[d+1][target+1];
        ans[0][0] = 1;
        int mod = 1000000007;
        for(int i = 1; i < d+1; i++){
            for(int j = 1; j < target+1; j++){
                int k = 1;
                while(k <= Math.min(f, j)){
                    ans[i][j] = (ans[i][j] + ans[i-1][j-k]) % mod;
                    k++;
                }
            }
        }
        return ans[d][target];
    }
}