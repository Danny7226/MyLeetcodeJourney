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
    int index = 0;
    public TreeNode bstFromPreorder(int[] preorder) {
        return helper(preorder, Integer.MAX_VALUE);
    }
    public TreeNode helper(int[] preorder, int limit){
        if (index >= preorder.length || preorder[this.index] > limit) return null;
        TreeNode root = new TreeNode(preorder[this.index++]);
        root.left = helper(preorder, root.val);
        root.right = helper(preorder, limit);
        return root;
    }
}