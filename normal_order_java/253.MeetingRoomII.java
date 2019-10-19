class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int[] starts = new int[intervals.length], ends = new int[intervals.length];
        for(int i = 0; i < intervals.length; i++){
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        Arrays.sort(starts);
        Arrays.sort(ends);
        int ans = 0, ptr = 0;
        for(int i = 0; i < starts.length; i++){
            if(starts[i] < ends[ptr]) ans++;
            else ptr++;
        }
        return ans;
    }
}