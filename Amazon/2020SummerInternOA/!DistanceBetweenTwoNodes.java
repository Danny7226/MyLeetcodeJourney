// Given a list of unique integers nums, construct a BST from it (you need to insert nodes one-by-one with the given order to get the BST) and find the distance between two nodes node1 and node2. Distance is the number of edges between two nodes. If any of the given nodes does not appear in the BST, return -1.

// Example 1:

// Input: nums = [2, 1, 3], node1 = 1, node2 = 3
// Output: 2
// Explanation:
//      2
//    /   \
//   1     3
// Java solution
// Related problems:

// https://leetcode.com/problems/insert-into-a-binary-search-tree/
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
import java.util.*;
public class DistanceBetweenTwoNodes{
    public static void main(String[] args){
        int[] nums = new int[]{2,1,3};
        Solutions s = new Solutions();
        System.out.println(s.getAnswer(nums, 1, 3));
    }
}

class Solutions{
    public int getAnswer(int[] nums, int node1, int node2){
        if(nums.length <= 0) return -1;
        TreeNode root = new TreeNode(nums[0]);
        for(int i = 1; i < nums.length; i++) insertBST(root, nums[i]);
        // TreeNode.print(root);
        TreeNode n1 = locateNode(root, node1);
        TreeNode n2 = locateNode(root, node2);
        
        return 1;
    }

    private TreeNode insertBST(TreeNode root, int val){
        if(root == null) return new TreeNode(val);
        if(val > root.val) root.right = insertBST(root.right, val);
        else root.left = insertBST(root.left, val);
        return root;
    }

    private TreeNode locateNode(TreeNode root, int val){
        if(root.val == val) return root;
        if(root.val > val) return locateNode(root.left, val);
        else return locateNode(root.right, val);
    }
}

class TreeNode{
    TreeNode left;
    TreeNode right;
    int val;
    public TreeNode(int val){
        this.val = val;
    }
    public static void print(TreeNode root){
        // bfs
        List<Integer> ans = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        TreeNode cur;
        while(!q.isEmpty()){
            int size = q.size();
            for(int i = 0; i < size; i++){
                cur = q.poll();
                ans.add(cur.val);
                if(cur.left != null) q.offer(cur.left);
                if(cur.right != null) q.offer(cur.right);
            }
        }
        for(int i = 0; i < ans.size(); i++){
            System.out.print(ans.get(i) + " ");
        }
        System.out.println("");
    }
}