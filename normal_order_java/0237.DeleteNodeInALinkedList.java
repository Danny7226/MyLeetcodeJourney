/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
	// best
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}

class Solution {
    public void deleteNode(ListNode node) {
        ListNode tail = node;
        while(node.next!=null){
            node.val = node.next.val;
            tail = node;
            node = node.next;
        }
        tail.next = null;
    }
}