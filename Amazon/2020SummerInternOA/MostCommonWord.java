// Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
// Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
// Example:
// Input: 
// paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
// banned = ["hit"]
// Output: "ball"
// Explanation: 
// "hit" occurs 3 times, but it is a banned word.
// "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
// Note that words in the paragraph are not case sensitive,
// that punctuation is ignored (even if adjacent to words, such as "ball,"), 
// and that "hit" isn't the answer even though it occurs more because it is banned.
// Note:
// 1 <= paragraph.length <= 1000.
// 0 <= banned.length <= 100.
// 1 <= banned[i].length <= 10.
// The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
// paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
// There are no hyphens or hyphenated words.
// Words only consist of letters, never apostrophes or other punctuation symbols.

import java.util.*;
public class MostCommonWord{
	public static void main(String[] args){
		Solution s = new Solution();
		String ans = s. mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", new String[]{"hit"});
		System.out.println(ans);
	}
}

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String ans = "";
        int count = 0;
        Set<String> ban = new HashSet<>();
        for(String b: banned) ban.add(b);
        String[] words = paragraph.toLowerCase().split("\\W+");
        Map<String, Integer> hm = new HashMap<>();
        for(String word: words){
            if(hm.containsKey(word)) hm.put(word, hm.get(word)+1);
            else hm.put(word, 1);
        }
        for(String key: hm.keySet()){
            if(ban.contains(key)) continue;
            if(count < hm.get(key)){
                ans = key;
                count = hm.get(key);
            }
        }
        return ans;
    }
}