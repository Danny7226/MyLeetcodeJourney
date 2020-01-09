// Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.

// Don't include the first or final entry. You can only move either down or right at any point in time.

// Example 1:

// Input:
// [[5, 1],
//  [4, 5]]

// Output: 4
// Explanation:
// Possible paths:
// 5 → 1 → 5 => min value is 1
// 5 → 4 → 5 => min value is 4
// Return the max value among minimum values => max(4, 1) = 4.
// Example 2:

// Input:
// [[1, 2, 3]
//  [4, 5, 1]]

// Output: 4
// Explanation:
// Possible paths:
// 1-> 2 -> 3 -> 1
// 1-> 2 -> 5 -> 1
// 1-> 4 -> 5 -> 1
// So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
// Return the max of that, so 4.

public class PathWithMaximumScore{
    public static void main(String[] args){
        int[][] matrix = new int[][]{{0},{1},{2}}; // {{0}}; {}
        int ans = Solutions.getAnswer(matrix);
        System.out.println(ans);
    }
}

class Solutions{
    public static int getAnswer(int[][] matrix){
        int rows = matrix.length, columns = matrix[0].length;
        if(rows == 1 && columns == 1) return 0;
        int[][] dp = new int[rows][columns];
        dp[0][0] = Integer.MAX_VALUE;
        for(int i = 1; i < columns; i++){
            dp[0][i] = Math.min(dp[0][i-1],matrix[0][i]);
        }
        for(int i = 1; i < rows; i++){
            dp[i][0] = Math.min(dp[i-1][0], matrix[i][0]);
        }
        for(int row = 1; row < rows; row++){
            for(int column = 1; column < columns; column++){
                dp[row][column] = Math.max(Math.min(dp[row-1][column], matrix[row][column]), Math.min(dp[row][column-1], matrix[row][column]));
            }
        }
        dp[rows-1][columns-1] = Math.max(dp[rows-2][columns-1], dp[rows-1][columns-2]);
        return dp[rows-1][columns-1];
    }
}