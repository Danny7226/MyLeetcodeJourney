// 5. Longest Palindromic Substring

// Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

// Example 1:

// Input: "babad"
// Output: "bab"
// Note: "aba" is also a valid answer.
// Example 2:

// Input: "cbbd"
// Output: "bb"

import java.util.*;
public class LongestPalindromicSubstring{
    public static void main(String[] args){
        Solutions s = new Solutions();
        String ans = s.getAnswer("babad");
        System.out.println(ans);
    }
}

class Solutions{
    private int lo = 0, maxLen = 0;
    public String getAnswer(String s){
        int len = s.length();
        if(len < 2) return s;
        for(int i = 0; i < len; i++){
            helper(s, i, i); // for odd palindrome check
            helper(s, i, i+1); // for even palindrome check
        }
        return s.substring(lo, lo + maxLen);
    }

    private void helper(String s, int j, int k){
        while(j>=0 && k<=s.length()-1 && s.charAt(j)==s.charAt(k)){
            j--;
            k++;
        }
        j += 1;
        k -= 1;
        if(maxLen < k - j + 1){
            lo = j;
            maxLen = k - j + 1;
        }
    }
}