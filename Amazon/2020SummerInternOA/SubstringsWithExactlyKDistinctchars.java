// Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
// https://leetcode.com/problems/subarrays-with-k-different-integers

// Example 1:

// Input: s = "pqpqs", k = 2
// Output: 7
// Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
// Example 2:

// Input: s = "aabab", k = 3
// Output: 0
// Constraints:

// The input string consists of only lowercase English letters [a-z]
// 0 ≤ k ≤ 26

class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        return atMost(A, K) - atMost(A, K-1);
    }
    
    public int atMost(int[] A, int K){
        int ans = 0;
        Map<Integer, Integer> map = new HashMap<>();
        int lo = 0;
        for(int hi = 0; hi < A.length; hi++){
            if(map.getOrDefault(A[hi], 0) == 0) K--;
            map.put(A[hi], map.getOrDefault(A[hi], 0) + 1);
            while(K<0){
                map.put(A[lo], map.getOrDefault(A[lo], 0) - 1);
                if(map.get(A[lo]) == 0) K++;
                lo++;
            }
            ans += hi - lo + 1;
        }
        return ans;
    }
}