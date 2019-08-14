class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(heaters);
        int pos = 0, ans = 0, cur = 0;
        int dummy = Integer.MAX_VALUE;
        for(int house: houses){
            pos = Arrays.binarySearch(heaters, house);
            if (pos < 0) pos = -(pos+1);
            // System.out.println("pos: "+pos);
            int left = (pos >= 1)? house - heaters[pos-1]:dummy;
            int right = (pos < heaters.length)? heaters[pos]-house: dummy;
            ans = Math.max(ans, Math.min(left, right));
        }
        return ans;
    }
}

class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(heaters);
        int pos = 0, ans = 0, cur = 0;
        for(int house: houses){
            pos = Arrays.binarySearch(heaters, house);
            if (pos < 0) pos = -(pos+1);
            // System.out.println("pos: "+pos);
            if (pos==0) {
                cur = heaters[0]-house;
            }
            else if (pos>=heaters.length){
                cur = house - heaters[heaters.length-1];
            }else{
                cur = Math.min(heaters[pos]-house, house - heaters[pos-1]);
            }
            // System.out.println("cur: "+cur);
            ans = Math.max(ans, cur);
        }
        return ans;
    }
}