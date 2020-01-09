class Solution {
    public int trap(int[] height) {
        if(height.length < 2) return 0;
        Stack<Integer> stack = new Stack<>();
        int i = 0, ans = 0;
        while(i < height.length){
            if(stack.isEmpty() || height[stack.peek()] >= height[i]){
                stack.push(i++);
            } else{
                int bot = stack.pop();
                int min = stack.isEmpty()? 0 : Math.min(height[i], height[stack.peek()]);
                // System.out.println(min);
                if(min > height[bot]){
                    ans += (min - height[bot]) * (i - stack.peek() - 1);
                }
            }
        }
        return ans;
    }
} 

// class Solution {
//     public int trap(int[] height) {
//         //dynamic programming
//         // O(3n) == O(n)
//         if(height.length == 0) return 0;
//         int ans = 0;
//         int[] maxl = new int[height.length], maxr = new int[height.length];
//         maxl[0] = height[0];
//         maxr[height.length - 1] = height[height.length - 1];
        
//         // store the highest bar up to position i from left end;
//         for(int i = 1; i < height.length; i++){
//             maxl[i] = Math.max(maxl[i-1], height[i]);
//         }
        
//         //store the highest bar up tp position i from right end;
//         for(int i = height.length -2; i >= 0; i--){
//             maxr[i] = Math.max(maxr[i+1], height[i]);
//         }
//         for(int i = 1; i < height.length-1; i++){
//             int min = Math.min(maxl[i-1], maxr[i+1]);
//             if(min > height[i]) ans += min - height[i];
//         }
//         return ans;
//     }
// }

// class Solution {
//     public int trap(int[] height) {
//         // O(n^2)
//         int ans = 0;
//         for(int i = 0; i < height.length; i++){
//             int l = i, r = i, maxl = 0, maxr = 0;
//             while(l>=0){
//                 if(height[l] > maxl) maxl = height[l];
//                 l--;
//             }
//             while(r<=height.length-1){
//                 if(height[r] > maxr) maxr = height[r];
//                 r++;
//             }
//             int min = Math.min(maxl, maxr);
//             if(min > height[i]) ans += min - height[i];
//         }
//         return ans;
//     }
// }