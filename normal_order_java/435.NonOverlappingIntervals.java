class CostomComp implements Comparator<int[]>{
    public int compare(int[] a, int[] b){
        if(a[0] != b[0]) return a[0] - b[0];
        else return a[1] - b[1];
    }
}
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if(intervals.length == 0) return 0;
        Arrays.sort(intervals, new CostomComp());
        int ans = 0;
        int[] prev = intervals[0];
        for(int i = 1; i < intervals.length; i++){
            if(intervals[i][0] < prev[1]){
                ans++;
                if(intervals[i][1] < prev[1]) prev = intervals[i]; // this matters !!
            }
            else prev = intervals[i];
        }
        return ans;
    }
}