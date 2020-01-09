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
    public boolean isSubtree(TreeNode s, TreeNode t) {
        return s!=null && (compare(s, t) || isSubtree(s.left, t) || isSubtree(s.right, t));
    }
    public boolean compare(TreeNode s, TreeNode t){
        if(s==null && t==null) return true;
        if(s==null || t==null) return false;
        return s.val == t.val && compare(s.left, t.left) && compare(s.right, t.right);
    }
}