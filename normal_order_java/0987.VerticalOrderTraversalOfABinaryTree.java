/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    class Triplet implements Comparable<Triplet>{
        int x;
        int y;
        int val;
        Triplet(int x, int y, int val){
            this.x = x;
            this.y = y;
            this.val = val;
        }
        // override
        public int compareTo(Triplet that){
            if (this.x != that.x){
                return this.x - that.x;
            }else if (this.y != that.y){
                return this.y - that.y;
            }else{
                return this.val - that.val;
            }
            
        }
    }
    
    public void dfs(List<Triplet> set, int x, int y, TreeNode root){
        if (root ==null) return;
        set.add(new Triplet(x, y, root.val));
        if (root.left != null) dfs(set, x-1, y+1, root.left);
        if (root.right != null) dfs(set, x+1, y+1, root.right);
    } 
    
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<Triplet> set = new ArrayList<Triplet>();
        dfs(set, 0, 0, root);
        Collections.sort(set);
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        int i = 0;
        int prev_x;
        while (i < set.size()){
            List<Integer> tmp = new ArrayList<Integer>();
            tmp.add(set.get(i).val);
            prev_x = set.get(i++).x;
            while(i<set.size() && set.get(i).x == prev_x){
                tmp.add(set.get(i++).val);
            }
            ans.add(tmp);
        }
        return ans;  
    }

}