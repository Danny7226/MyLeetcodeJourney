// 763. Partition Labels
// Medium
// 1348
// 74
// Favorite
// Share
// A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
// Example 1:
// Input: S = "ababcbacadefegdehijhklij"
// Output: [9,7,8]
// Explanation:
// The partition is "ababcbaca", "defegde", "hijhklij".
// This is a partition so that each letter appears in at most one part.
// A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
class Solution {
    public List<Integer> partitionLabels(String S) {
        List<Integer> ans = new ArrayList<>();
        int len = S.length();
        Map<Character, Integer> table = new HashMap<>();
        for(int i = 0; i < len; i++){
            table.put(S.charAt(i), i);
        }
        int anchor = 0, partition = 0;
        for(int i = 0; i < len; i++){
            partition = Math.max(partition, table.get(S.charAt(i)));
            if(i == partition){
                ans.add(i - anchor + 1);
                anchor = i+1;
            }
        }
        return ans;
    }
}