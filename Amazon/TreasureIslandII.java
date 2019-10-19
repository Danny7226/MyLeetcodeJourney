// You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.

// Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

// Example:

// Input:
// [["S", "O", "O", "S", "S"],
//  ["D", "O", "D", "O", "D"],
//  ["O", "O", "O", "O", "X"],
//  ["X", "D", "D", "O", "O"],
//  ["X", "D", "D", "D", "O"]]

// Output: 3
// Explanation:
// You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
import java.util.*;
public class TreasureIslandII{
	public static void main(String[] args){
		String[][] input = new String[5][5];
		input[0] = new String[]{"S", "O", "O", "S", "S"};
		input[1] = new String[]{"D", "O", "D", "O", "D"};
		input[2] = new String[]{"O", "O", "O", "O", "X"};
		input[3] = new String[]{"X", "D", "D", "O", "O"};
		input[4] = new String[]{"X", "D", "D", "D", "O"};
		Solutions s = new Solutions();
		int ans = s.getAnswer(input);
		System.out.println(ans);
	}
}

class Solutions{
	public static int getAnswer(String[][] input){
		int ans = 0;
		Queue<int[]> bfs = new LinkedList<>();
		int rows = input.length, columns = input[0].length;
		for(int row = 0; row < rows; row++){
			for(int column = 0; column < columns; column++){
				if(input[row][column] == "S") {
					bfs.offer(new int[]{row, column});
					input[row][column] = "D";
				}
			}
		}
		int[] dx = new int[]{0, 0, 1, -1}, dy = new int[]{1, -1, 0, 0};
		int[] cur;
		while(!bfs.isEmpty()){
			int size = bfs.size();
			for(int i = 0; i < size; i++){
				cur = bfs.poll();
				System.out.println(ans + " " + cur[0] + " "+ cur[1]);
				for(int j = 0; j < 4; j++){
					if(cur[0]+dx[j]<0 || cur[0]+dx[j]>=rows || cur[1]+dy[j]<0 || cur[1]+dy[j]>=columns) continue;
					if(input[cur[0]+dx[j]][cur[1]+dy[j]] != "D"){
						if(input[cur[0]+dx[j]][cur[1]+dy[j]].equals("X")) return ans+1;
						bfs.offer(new int[]{cur[0]+dx[j], cur[1]+dy[j]});
						input[cur[0]+dx[j]][cur[1]+dy[j]] = "D";
					}
				}
			}
			ans += 1;
		}

		return -1;
	}
}