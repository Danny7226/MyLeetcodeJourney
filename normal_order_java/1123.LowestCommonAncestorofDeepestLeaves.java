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
    
    class Pair {
        int depth;
        TreeNode node;
        public Pair(TreeNode node, int depth){
            this.node = node;
            this.depth = depth;
        }
    }
    public TreeNode lcaDeepestLeaves(TreeNode root) {
        Pair p = helper(root);
        return p.node;
    }
    
    public Pair helper(TreeNode root){
        if (root == null){
            return new Pair(null, 0);
        }
        Pair l = helper(root.left);
        Pair r = helper(root.right);
        if (l.depth == r.depth){
            return new Pair(root, l.depth+1);
        }
        if (l.depth < r.depth){
            return new Pair(r.node, r.depth+1);
        }
        return new Pair(l.node, l.depth+1); // l.depth > r.depth
    }
}