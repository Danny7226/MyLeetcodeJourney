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
    // faster and smarter
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if(left != null && right != null) return root;
        return left != null? left: right;
        // left == null && right == null return null;
        // left == null && right != null return right;
        // left != null && right == null return left;
    }
}


class Solution {
    TreeNode ans;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Map<TreeNode, TreeNode> parent = new HashMap<TreeNode, TreeNode>();
        Set<TreeNode> set = new HashSet<TreeNode>();
        dfs(parent, set, root, p, q);
        return ans;
    }
    
    public void dfs(Map<TreeNode, TreeNode> parent, Set<TreeNode> set, TreeNode root, TreeNode p, TreeNode q){
        if(set.size() == 2 || root == null) return;
        if(root == p || root == q){
            set.add(root);
            if(set.size() == 2){
                Set<TreeNode> candi = new HashSet();
                while(parent.containsKey(p)){
                    // System.out.println(p.val);
                    candi.add(p);
                    p = parent.get(p);
                }
                candi.add(p);
                while(!candi.contains(q)){
                    q = parent.get(q);
                }
                this.ans = q;
                return;
            }
        }
        if(root.left != null){
            parent.put(root.left, root);
            // System.out.println(root.left.val + " " + 1);
            dfs(parent, set, root.left, p, q);
        }
        if(root.right != null){
            // System.out.println(root.right.val + " " + 2);
            parent.put(root.right, root);
            dfs(parent, set, root.right, p, q);
        }
        return;
    }
}