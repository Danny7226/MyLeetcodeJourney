/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // recursive
        if(head == null || head.next == null) return head;
        ListNode ans = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return ans;
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        // iterative
        if(head == null) return head;
        ListNode prev = null, next = head.next;
        while(next!=null){
            head.next = prev;
            prev = head;
            head = next;
            next = next.next;
        }
        head.next = prev;
        return head;
    }
}

public class ReverseLinkedList{
	public static void main(String[] args){
		Solution s = new Solution();
		// initial a linked list[1,2,3,4,5]
        int i = 1;
        ListNode head = new ListNode(i);
        ListNode input = head;
        while (i < 5){
            i++;
            ListNode tmp = new ListNode(i);
            head.next = tmp;
            head = head.next;
        }		
        System.out.println("Original: " + ListNode.print(input) );
        System.out.println("After: " + ListNode.print(s.reverseList(input)));
	}
}