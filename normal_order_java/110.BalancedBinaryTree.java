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
    private boolean ans = true;
    public int helper (TreeNode root){
        if (root == null){
            return 0;
        }
        int left = helper(root.left);
        int right = helper(root.right);
        if (Math.abs(left-right) >1){
            ans = false;
        }
        return Math.max(left, right)+1;
        
    }
    public boolean isBalanced(TreeNode root) {
        helper(root);
        return ans;
    }
}