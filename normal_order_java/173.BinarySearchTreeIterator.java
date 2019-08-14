/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator {
    Queue<Integer> value = new LinkedList<Integer>();
    public BSTIterator(TreeNode root) {
        helper(root);
    }
    
    public void helper(TreeNode root){
        if (root == null){
            return;
        }
        helper(root.left);
        this.value.offer(root.val);
        helper(root.right);
    }
    /** @return the next smallest number */
    public int next() {
        return value.poll();
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !value.isEmpty();
    }
}

class BSTIterator {
    Stack<TreeNode> s = new Stack<TreeNode>();
    public BSTIterator(TreeNode root) {
        helper(root);
    }
    
    public void helper(TreeNode root){    
        while (root != null){
            s.push(root);
            root = root.left;
        }
    }
    
    /** @return the next smallest number */
    public int next() {
        TreeNode cur = this.s.pop();
        if (cur.right != null){
            this.helper(cur.right);
        }
        return cur.val;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return (s.size() > 0);
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */