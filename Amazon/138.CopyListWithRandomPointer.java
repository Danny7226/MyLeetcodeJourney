/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution{
    public Node copyRandomList(Node head){
        // O(N) O(1) space
        
    }
}


class Solution{
    // iteration O(N)
    Map<Node, Node> visited = new HashMap<>();
    public Node copyRandomList(Node head){
        if(head == null) return null;
        Node dummy = head;
        Node node = new Node(head.val, null, null);
        visited.put(head, node);
        while(head != null){
            node.random = getCopy(head.random);
            node.next = getCopy(head.next);
            node = node.next;
            head = head.next;
        }
        return visited.get(dummy);
    }
    private Node getCopy(Node node){
        if(node == null) return null;
        if(visited.containsKey(node)) return visited.get(node);
        Node copy = new Node(node.val, null, null);
        visited.put(node, copy);
        return copy;
    }
}


class Solution {
    // recursion
    Map<Node, Node> visited = new HashMap<>();
    public Node copyRandomList(Node head) {
        if(head == null) return null;
        if(visited.containsKey(head)) return visited.get(head);
        Node node = new Node(head.val, null, null);        
        visited.put(head, node);
        node.next = copyRandomList(head.next);
        node.random = copyRandomList(head.random);
        return node;
    }
}