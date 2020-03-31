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
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (root.val == key){
            if (root.right != null){
                TreeNode left = root.left, ans = root.right;
                root = root.right;
                while (root != null && root.left != null) root = root.left;
                root.left = left;
                return ans;
            }else if (root.left != null){
                return root.left;
            }else return null;
        }
        if (root.val < key) {
            root.right = deleteNode(root.right, key);
        }
        else{
            root.left = deleteNode(root.left, key);
        }
        return root;
    }
}