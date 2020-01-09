class Solution {
    int maxl=0, maxr=0;
    public String longestPalindrome(String s) {
        // O(n*n), O(1)        
        if(s.length() == 0) return "";
        for(int i = 0; i < s.length(); i++){
            check(s, i, i);
            check(s, i, i+1);
        }
        return s.substring(maxl, maxr+1);
        
    }
    public void check(String s, int l, int r){
        while(l>=0 && r<s.length() && s.charAt(l) == s.charAt(r)){
            l--;
            r++;
        }
        // System.out.println(l + " " + r);
        l++;
        r--;
        if(r-l > maxr - maxl){
            maxl = l;
            maxr = r;
        }
    }    
}

// class Solution {
//     public String longestPalindrome(String s) {
//         // dynamic programming O(n*n), O(n*n)
//         int n = s.length();
//         String res = "";
//         boolean[][] dp = new boolean[n][n];
//         for(int i = 0; i < n; i++){
//             for(int j = i; j >=0; j--){
//                 dp[i][j] = s.charAt(i) == s.charAt(j) && (i - j < 3 || dp[i-1][j+1]);
//                 if(dp[i][j] && i-j+1 > res.length()) res = s.substring(j, i+1);
//             }
//         }
//         return res;        
//     }
// }  