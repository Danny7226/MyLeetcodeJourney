// Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
// A subtree of a tree is the node which have at least 1 child plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.
// Example 1:
// Input:
// 		 20
// 	   /   \
// 	 12     18
//   /  |  \   / \
// 11   2   3 15  8
// Output: 18
// Explanation:
// There are 3 nodes which have children in this tree:
// 12 => (11 + 2 + 3 + 12) / 4 = 7
// 18 => (18 + 15 + 8) / 3 = 13.67
// 20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125
// 18 has the maximum average so output 18.
// Similar questions:
// https://leetcode.com/problems/maximum-average-subtree
import java.util.*;
public class SubtreeWithMaximumAverage{
	public static void main(String[] args){
		TreeNode root = new TreeNode(20);
		root.left = new TreeNode(12);
		root.right = new TreeNode(18);
		TreeNode temp = root.left;
		temp.left = new TreeNode(11);
		temp.mid = new TreeNode(2);
		temp.right = new TreeNode(3);
		temp = root.right;
		temp.left = new TreeNode(15);
		temp.right = new TreeNode(8);
		Solutions s = new Solutions();
		System.out.println(s.getAnswer(root).val);
	}
}

class Solutions{
	double max = 0;
	TreeNode ans;
	public TreeNode getAnswer(TreeNode root){
		postOrder(root);
		return ans;
	}

	public double[] postOrder(TreeNode root){
		if(root == null) return new double[]{0, 0};
		double[] left = postOrder(root.left);
		double[] mid = postOrder(root.mid);
		double[] right = postOrder(root.right);
		double sum = left[0] + mid[0] + right[0] + root.val, count = left[1] + mid[1] + right[1] + 1;
		if(count > 1){
			double avg = sum / count;
			if(max < avg){
				max = avg;
				ans = root;
			}
		}
		return new double[]{sum, count};
	}
}

class TreeNode{
	int val;
	TreeNode left;
	TreeNode mid;
	TreeNode right;
	TreeNode(int val){
		this.val = val;
	}
}