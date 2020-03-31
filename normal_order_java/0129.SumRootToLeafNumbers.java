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
    int ans = 0;
    public int sumNumbers(TreeNode root) {
        if(root == null) return this.ans;
        dfs(root, 0);
        return this.ans;
    }
    public void dfs(TreeNode root, int sum){
        if (root.left == null && root.right == null){
            this.ans += sum*10+root.val;
            return;
        }
        if(root.left != null){
            dfs(root.left, sum*10+root.val);
        }
        if(root.right != null){
            dfs(root.right, sum*10+root.val);
        }
    }
    
}