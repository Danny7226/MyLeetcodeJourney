class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] ans = new int[amount + 1];
        ans[0] = 0;
        for(int i = 1; i <= amount; i++){
            int min = Integer.MAX_VALUE-1;
            for(int coin: coins){
                if(i-coin >= 0) min = Math.min(ans[i-coin]+1, min);
            }
            ans[i] = min;
        }
        return ans[amount] == Integer.MAX_VALUE-1? -1:ans[amount];
    }
}