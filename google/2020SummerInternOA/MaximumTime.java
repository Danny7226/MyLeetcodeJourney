// You are given a string that represents time in the format hh:mm. Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

// Example 1:

// Input: "?4:5?"
// Output: "14:59"
// Example 2:

// Input: "23:5?"
// Output: "23:59"
// Example 3:

// Input: "2?:22"
// Output: "23:22"
// Example 4:

// Input: "0?:??"
// Output: "09:59"
// Example 5:

// Input: "??:??"
// Output: "23:59"
import java.util.*;
public class MaximumTime{
	public static void main(String[] args){
		Solutions s = new Solutions();
		System.out.println(s.getAnswer("?4:5?"));
		System.out.println(s.getAnswer("??:??"));
	}
}

class Solutions{
	public String getAnswer(String input){
		char[] ans = input.toCharArray();

		if(ans[0] == '?') {
			ans[0] = (ans[1] <= '3' || ans[1] == '?')? '2':'1';
		}

		if(ans[1] == '?'){
			ans[1] = (ans[0] == '2' || ans[1] == '?')? '3':'9';
		}

		ans[3] = ans[3] == '?'? '5':ans[3];
		ans[4] = ans[4] == '?'? '9':ans[4];
		return new String(ans);
	}
}