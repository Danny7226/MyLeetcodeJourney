class Solution {
    public List<Integer> pancakeSort(int[] A) {
        List<Integer> ans = new ArrayList<>();
        int cur = A.length;
        int i;
        while(cur > 1){
            for(i = 0; A[i]!=cur; i++);
            // System.out.println(i);
            ans.add(i+1);
            reverse(A, 0, i);
            ans.add(cur);
            reverse(A, 0, --cur);            
        }
        return ans;
    }
    
    public void reverse(int[] A, int l, int r){
        while(l < r){
            int tmp = A[l];
            A[l++] = A[r];
            A[r--] = tmp;
        }
    }
}