import java.util.*;

public class CompareStrings{
	public static void main(String[] args){
		Solutions s = new Solutions();
		int[] ans = s.getAnswer("abcd,aabc,bd","aaa,aa");

	}
}

class Solutions{
	public int[] getAnswer(String A, String B){
		String[] strA = A.split(","), strB = B.split(",");
		int[] freqs = new int[11];
		int[] ans = new int[strB.length];

		// count the frequence of smallest letter
		for(int i = 0; i < strA.length; i++){
			int freq = findFreq(strA[i]);
			freqs[freq]++;
		}

		// prefix sum
		for(int i = 1; i < 11; i++){
			freqs[i] += freqs[i-1];
		}

		// find 
		for(int i = 0; i < strB.length; i++){
			int freq = findFreq(strB[i]);
			ans[i] = freqs[freq-1];
		}


		// print
		for(int i = 0; i < ans.length; i++){
			System.out.print(ans[i] + " ");
		}
		System.out.println();
		return ans;
	}

	private int findFreq(String s){
		int[] ch = new int[26];
		int min = 27;
		for(char c: s.toCharArray()){
			ch[c - 'a']++;
			if(c - 'a' < min) min = c-'a';
		}
		return ch[min];
	}
}