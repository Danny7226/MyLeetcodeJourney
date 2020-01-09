/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
    int index;
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serialize_helper(sb, root);
        System.out.println(sb.toString());
        return sb.toString();
    }
    private void serialize_helper(StringBuilder sb, TreeNode root){
        if(root == null){
            sb.append("$,");
            return;
        } else{
            sb.append(String.valueOf(root.val) + ",");
            serialize_helper(sb, root.left);
            serialize_helper(sb, root.right);
        }
    }
    

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] values = data.split(",");
        this.index = 0;
        return de_helper(values);
    }
    
    private TreeNode de_helper(String[] values){
        if(values.length == 0) return null;
        if(values[index].equals("$")) {
            index++;
            return null;
        }
        TreeNode root = new TreeNode(Integer.valueOf(values[this.index++]));
        // System.out.println(root.val);
        root.left = de_helper(values);
        root.right = de_helper(values);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));