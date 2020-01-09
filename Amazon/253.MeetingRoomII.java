class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int ans = 0;
        int[] start = new int[intervals.length], end = new int[intervals.length];
        for(int i = 0; i < intervals.length; i++){
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }
        Arrays.sort(start);
        Arrays.sort(end);
        int ptr = 0;
        for(int i = 0; i < start.length; i++){
            if(start[i] < end[ptr]) ans++;
            else ptr++;
        }
        return ans;
    }
}

// class Solution {
//     public int minMeetingRooms(int[][] intervals) {
//         int ans = 0;
//         PriorityQueue<Integer> pq = new PriorityQueue<>();
//         Arrays.sort(intervals,(int[] a, int[] b)->{
//            return a[0] - b[0]; 
//         });
//         for(int[] interval: intervals){
//             while(pq.size()!=0 && interval[0] >= pq.peek()) {
//                 pq.poll();
//             }
//             pq.offer(interval[1]);
//             if(pq.size() > ans) ans=pq.size();
//         }
//         return ans;
//     }
// }