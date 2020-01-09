// Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

// Example 1:

// Input: s = "abcabc", k = 3
// Output: ["abc", "bca", "cab"]
// Example 2:

// Input: s = "abacab", k = 3
// Output: ["bac", "cab"]
// Example 3:

// Input: s = "awaglknagawunagwkwagl", k = 4
// Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
// Explanation: 
// Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
// "wagl" is repeated twice, but is included in the output once.
// Constraints:

// The input string consists of only lowercase English letters [a-z]
// 0 ≤ k ≤ 26
import java.util.*;
public class SubstringOfSizeKWithKDistinctChars{
	public static void main(String[] args){
		Solutions s = new Solutions();
		System.out.println(s.getAnswer("awaglknagawunagwkwagl", 4));
	}
}

class Solutions{
	public List<String> getAnswer(String s, int k){
		Set<String> set = new HashSet<>();
		List<String> ans = new ArrayList<>();
		int[] ch = new int[26];
		int lo = 0, hi = 0;
		while(lo <= hi && hi < s.length()){
			ch[s.charAt(hi) - 'a']++;
			while(ch[s.charAt(hi) - 'a'] != 1){
				ch[s.charAt(lo) - 'a']--;
				lo++;
			}
			if(hi - lo + 1 == k){
				set.add(s.substring(lo, hi+1));
				ch[s.charAt(lo) - 'a']--;
				lo++;
			}
			hi++;
		}
		// System.out.println(set.size());
		Iterator<String> it = set.iterator();
		while(it.hasNext()){
			String cur = it.next();
			ans.add(cur);
		}
		return ans;
	}
}