class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> seen = new HashSet<Integer>();
        Queue<List<Integer>> q = new LinkedList();
        q.offer(rooms.get(0));
        seen.add(0);
        while(!q.isEmpty()){
            List<Integer> room = q.poll();
            for (Integer r: room){
                if(!seen.contains(r)){
                    q.offer(rooms.get(r));
                    seen.add(r);
                }
            }
        }
        return seen.size() == rooms.size();
    }
}