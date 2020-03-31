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
	// Recursive
    List<Integer> ans = new ArrayList<Integer>();
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) return ans;
        postorderTraversal(root.left);
        postorderTraversal(root.right);
        ans.add(root.val);
        return ans;
    }
}

class Solution {
	// Iterative
    class Pair{
        boolean seen;
        TreeNode node;
        Pair(TreeNode node, boolean seen){
            this.node = node;
            this.seen = seen;
        }
    }
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<Integer>();
        if (root == null) return ans;
        Stack<Pair> post = new Stack<Pair>();
        post.push(new Pair(root, false));
        while (!post.isEmpty()){
            Pair curr = post.peek();
            if (curr.seen){
                ans.add(post.pop().node.val);
            }
            else{
                curr.seen = true;
                if (curr.node.right != null){
                    post.push(new Pair(curr.node.right, false));
                }
                if (curr.node.left != null){
                    post.push(new Pair(curr.node.left, false));
                }                
            }
        }
        return ans;
    }
}