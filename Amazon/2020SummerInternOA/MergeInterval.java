// Given a collection of intervals, merge all overlapping intervals.
// Example 1:
// Input: [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
// Example 2:
// Input: [[1,4],[4,5]]
// Output: [[1,5]]
// Explanation: Intervals [1,4] and [4,5] are considered overlapping.
// NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
class Solution {
    public int[][] merge(int[][] intervals) {
        if(intervals.length == 0) return intervals;
        Arrays.sort(intervals, (a,b) -> a[0] - b[0]);
        int ptr1 = 0, ptr2 = 1;
        while(ptr2 < intervals.length){
            if(intervals[ptr2][0] <= intervals[ptr1][1]){
                if(intervals[ptr2][1] > intervals[ptr1][1]){
                    intervals[ptr1][1] = intervals[ptr2][1];
                    ptr2++;                    
                }
                else ptr2++;
            }
            else{
                ptr1++;
                intervals[ptr1][0] = intervals[ptr2][0];
                intervals[ptr1][1] = intervals[ptr2][1];
                ptr2++;
            }
        }
        int[][] ans = new int[ptr1+1][2];
        for(int i = ptr1; i >= 0; i--){
            ans[i] = new int[]{intervals[i][0], intervals[i][1]};
        }
        return ans;
    }
}