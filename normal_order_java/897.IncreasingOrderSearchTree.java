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
    public TreeNode increasingBST(TreeNode root) {
        TreeNode ans = dummy;
        traversal(root);
        return ans.right;
    }
    
    public void traversal(TreeNode root){
        if (root == null){
            return;
        }
        traversal(root.left);
        root.left = null;
        dummy.right = root;
        dummy = root;
        traversal(root.right);
    }
}