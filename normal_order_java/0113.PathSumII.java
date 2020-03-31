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
    int target;
    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        this.target = sum;
        List<Integer> path = new ArrayList();
        dfs(root, 0, path);
        return this.ans;
    }
    
    public void dfs(TreeNode node, int sum, List<Integer> path){
        if (node == null) return;
        sum += node.val;
        path.add(node.val);
        if(node.left == null && node.right == null){
            if (sum == this.target){
                // System.out.println(path);
                this.ans.add(new ArrayList<Integer>(path));
                return;
            }
        }
        if (node.left != null){
            dfs(node.left, sum, path);
            path.remove(path.size()-1);            
        }
        if (node.right != null){
            dfs(node.right, sum, path);
            path.remove(path.size()-1);            
        }
    }
}