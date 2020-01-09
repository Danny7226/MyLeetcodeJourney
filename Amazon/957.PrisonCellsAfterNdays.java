class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
        int day = 0;
        N = (N-1) % 14 + 1;
        while(day != N){
            int[] dp = new int[8];
            for(int i = 1; i<cells.length-1; i++){
                dp[i] = (cells[i-1] == cells[i+1])? 1:0;
            }
            cells = dp;
            day++;
        }
        return cells;
    }
}