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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if (root == null) return ans;
        int dir = 0;
        Queue<TreeNode> bfs = new LinkedList<TreeNode>();
        bfs.offer(root);
        while(!bfs.isEmpty()){
            int size = bfs.size();
            List<Integer> level = new ArrayList<Integer>();
            for(int i=0; i<size; i++){
                TreeNode cur = bfs.poll();
                level.add(cur.val);
                if(cur.left != null) bfs.offer(cur.left);
                if(cur.right != null) bfs.offer(cur.right);
            }
            ans.add(level);
        }
        for(int i = 0; i<ans.size(); i++){
            if( (i&1)== 1) Collections.reverse(ans.get(i));
        }
        return ans;
    }
}