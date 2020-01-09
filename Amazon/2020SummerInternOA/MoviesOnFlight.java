// I had 2 question on my online assesment, however I remeber only the first one. My code passed only 10 test out of 13. I did a sorting and then found the best pair with 2 for loops

// Question:
// You are on a flight and wanna watch two movies during this flight.
// You are given List<Integer> movieDurations which includes all the movie durations.
// You are also given the duration of the flight which is d in minutes.
// Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

// Find the pair of movies with the longest total duration and return they indexes. If multiple found, return the pair with the longest movie.

// Example 1:

// Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
// Output: [0, 6]
// Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)
import java.util.*;
public class MoviesOnFlight{
	public static void main(String[] args){
		int [] movieDurations = new int[]{90, 85, 75, 60, 120, 150, 125};
		int d = 250;
		int[] ans = Solutions.getAnswer(movieDurations, 10);
		System.out.println(ans);
	}
}

class Solutions{
	// O(nlogn)
	public static int[] getAnswer(int [] movieDurations, int d){
		d = d - 30;
		Map<Integer, Integer> index = new HashMap<>();
		for(int i = 0; i < movieDurations.length; i++){
			index.put(movieDurations[i], i);
		}
		Arrays.sort(movieDurations); // merge sort
		if(movieDurations[0] + movieDurations[1] > d) return new int[]{};
		int ptr1 = 0, ptr2 = movieDurations.length-1;
		int cur, max = 0;
		int[] ans = new int[2];
		while(ptr1 < ptr2){
			cur = movieDurations[ptr1] + movieDurations[ptr2];
			// if(cur = d) return new int[]{index[ptr1], index[ptr2]};
			if(cur <= d){
				if(cur > max){
					ans[0] = index.get(movieDurations[ptr1]);
					ans[1] = index.get(movieDurations[ptr2]);
					max = cur;
					// System.out.println(ans[0] + " " + ans[1]);
				}
				ptr1++;
			}
			else ptr2--;
			
		}
		return ans;
	}
}