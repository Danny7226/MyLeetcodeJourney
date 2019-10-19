class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int l = 0, r = people.length-1, ans = 0;
        while(l < r){
            int cur = people[l] + people[r];
            if(cur <= limit){
                l = l+1;
                r = r-1;
                ans += 1;
            }
            else{
                r -= 1;
                ans += 1;
            }
        }
        if(l == r) ans += 1;
        return ans;
    }
}