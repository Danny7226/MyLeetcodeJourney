// #1
class Solution {
    // We determined above that once a number is below 243243, it is impossible for it to go back up above 243243. Therefore, based on our very shallow analysis we know for sure that once a number is below 243243, it is impossible for it to take more than another 243243 steps to terminate. Each of these numbers has at most 3 digits. With a little more analysis, we could replace the 243243 with the length of the longest number chain below 243243, however because the constant doesn't matter anyway, we won't worry about it.
    // O(logn) 2 times faster than solution2
    public boolean isHappy(int n) {
        int slow = getNext(n);
        int fast = getNext(getNext(n));
        while(fast != 1 && slow != fast){
            slow = getNext(slow);
            fast = getNext(getNext(fast));
            // System.out.println(fast);
        }
        return fast == 1;
    }
    
    // getNext method costs logn time complexity
    private int getNext(int n){
        int next = 0;
        while(n!=0){
            next += (n%10) * (n%10);
            n /= 10;
        }
        return next;
    }
}

// #2
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        while(n!=1 && !seen.contains(n)){
            seen.add(n);
            n = getNext(n);
        }
        return n == 1;
    }
    
    private int getNext(int n){
        int next = 0;
        while(n!=0){
            next += (n%10) * (n%10);
            n /= 10;
        }
        return next;
    }
}

// #3
class Solution {
    private HashSet<Integer> set;
    public boolean isHappy(int n) {
        set = new HashSet<>();
        if(n<0) return false;
        return isHappyNumber(n);
    }
    
    private boolean isHappyNumber(int n){
        int next = 0;
        while(n!=0){
            next += (n%10) * (n%10);
            n /= 10;
        }
        if(next == 1) return true;
        if(set.contains(next)) {
            return false;
        } else {
            // System.out.println(next);
            set.add(next);
            return isHappyNumber(next);
        }
    }
}
