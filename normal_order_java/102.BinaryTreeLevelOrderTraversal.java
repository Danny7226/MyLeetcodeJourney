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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList();
        if (root == null) return ans;
        Queue<TreeNode> bfs = new LinkedList<TreeNode>();
        bfs.offer(root);
        while (!bfs.isEmpty()){
            List<Integer> cur_level = new ArrayList<Integer>();
            int range = bfs.size();
            for (int i= 0; i<range; i++){
                TreeNode cur = bfs.poll();
                cur_level.add(cur.val);
                if (cur.left != null){
                    bfs.offer(cur.left);
                }
                if (cur.right != null){
                    bfs.offer(cur.right);
                }            
            }             
            ans.add(cur_level);
        }  
        return ans;
    }
}