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
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}

class Solution {
	// bfs
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        Queue<TreeNode> bfs_node = new LinkedList<TreeNode>();
        Queue<Integer> bfs_depth = new LinkedList<Integer>();
        bfs_node.offer(root);
        bfs_depth.offer(1);
        TreeNode cur_node = null;
        int cur_depth = 1;
        while (!bfs_node.isEmpty()){
            cur_node = bfs_node.poll();
            cur_depth = bfs_depth.poll();
            if (cur_node.left != null){
                bfs_node.offer(cur_node.left);
                bfs_depth.offer(cur_depth+1);
            }
            if (cur_node.right !=null){
                bfs_node.offer(cur_node.right);
                bfs_depth.offer(cur_depth+1);
            }
            
        }
        return cur_depth;
    }
}

class Solution {
	// DFS
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        Stack<TreeNode> dfs_node = new Stack<TreeNode>();
        Stack<Integer> dfs_depth = new Stack<Integer>();
        dfs_node.push(root);
        dfs_depth.push(1);
        int ans = 1;
        TreeNode cur_node = null;
        int cur_depth = 1;        
        while (!dfs_node.isEmpty()){
            cur_node = dfs_node.pop();
            cur_depth = dfs_depth.pop();
            if (cur_node.left == null && cur_node.right == null){
                ans = Math.max(ans, cur_depth);
            }
            if (cur_node.left != null){
                dfs_node.push(cur_node.left);
                dfs_depth.push(cur_depth+1);
            }
            if (cur_node.right !=null){
                dfs_node.push(cur_node.right);
                dfs_depth.push(cur_depth+1);
            }
        }
        return ans;
    }
}
