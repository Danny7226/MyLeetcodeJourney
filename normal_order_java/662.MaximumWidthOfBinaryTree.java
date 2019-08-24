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
    // DFS
    int ans;
    Map<Integer, Integer> left;
    public int widthOfBinaryTree(TreeNode root) {
        ans = 0;
        left = new HashMap();
        dfs(root, 0, 0);
        return ans;
    }
    public void dfs(TreeNode root, int depth, int pos) {
        if (root == null) return;
        left.putIfAbsent(depth, pos);
        ans = Math.max(ans, pos - left.get(depth) + 1);
        dfs(root.left, depth + 1, 2 * pos);
        dfs(root.right, depth + 1, 2 * pos + 1);
    }
}


class Solution {
    // BFS
    class Pair {
        TreeNode node;
        int position;
        Pair(TreeNode node, int position){
            this.node = node;
            this.position = position;
        }
    }
    public int widthOfBinaryTree(TreeNode root) {
        int ans = 0;
        if (root == null) return 0;
        Queue<Pair> q = new LinkedList<Pair>();
        q.offer(new Pair(root, 0));
        int begin = 0, end = 0;
        while(!q.isEmpty()){
            // System.out.println(q.size());
            int range = q.size();
            for(int i = 0; i < range; i++){
                Pair cur = q.poll();
                // System.out.print(cur.node.val + ""+ cur.position + " ");
                if (i == 0) {
                    begin = cur.position;
                }
                if (i == range-1) {
                    end = cur.position;
                    ans = Math.max(ans, end - begin + 1);
                }
                if(cur.node.left != null){
                    q.offer(new Pair(cur.node.left, cur.position*2));
                }
                if(cur.node.right != null){
                    q.offer(new Pair(cur.node.right, cur.position*2+1));
                }
            }
            // System.out.println();
        }
        return ans;
    }
}