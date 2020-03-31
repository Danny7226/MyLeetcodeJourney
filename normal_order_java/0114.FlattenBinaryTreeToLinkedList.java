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
    TreeNode dummy = new TreeNode(0);
    public void flatten(TreeNode root) {
        if (root == null){
            return;
        }
        dummy.right = root;
        dummy.left = null;
        dummy = root;
        TreeNode r = root.right;
        flatten(root.left);
        flatten(r);
    }
}