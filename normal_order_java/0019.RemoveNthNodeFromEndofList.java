// 19.RemoveNthNodeFromEndofList
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
import java.util.*;

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode slow = dummy, fast = dummy;
        for(int i=0; i<n; i++){
            fast = fast.next;
        }
        while(fast.next!=null){
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }

}

public class RemoveNthNodeFromEndofList {
    public static void main(String[] args){
        int i = 1;
        ListNode head = new ListNode(i);
        ListNode input = head;
        while (i < 5){
            i++;
            ListNode tmp = new ListNode(i);
            head.next = tmp;
            head = head.next;
        }
        List tmp = ListNode.print(input);
        System.out.println("Original: " + tmp );
        Solution s = new Solution();
        ListNode ans = s.removeNthFromEnd(input,2);
        System.out.println("After: " + ListNode.print(ans));        
    }
}
