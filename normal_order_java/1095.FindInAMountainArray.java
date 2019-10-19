/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int lo = 0, hi = mountainArr.length()-1;
        // find peak
        while(lo < hi){
            int mid = (lo + hi) / 2;
            if(mountainArr.get(mid) < mountainArr.get(mid+1)) lo = mid + 1;
            else hi = mid;
        }
        int peak = lo;
        // System.out.println(peak);
        // BS in left part
        lo = 0;
        hi = peak;
        while(lo <= hi){
            int mid = (lo + hi) / 2, cur = mountainArr.get(mid);
            if(cur == target) return mid;
            else if(cur < target) lo = mid + 1;
            else hi = mid-1;
        }
        // BS in right part
        lo = peak + 1;
        hi = mountainArr.length()-1;
        // System.out.println(lo + " " + hi);
        while(lo <= hi){
            int mid = (lo + hi) / 2, cur = mountainArr.get(mid);
            // System.out.println(mid + " " + cur);
            if(cur == target) return mid;
            else if(cur < target) hi = mid - 1;
            else lo = mid+1;
        }
        return -1;
    }
}