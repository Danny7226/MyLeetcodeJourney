/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode ans = dummy, ptr = dummy;
        while (dummy != null){
            dummy = dummy.next;
            while (dummy != null && dummy.val == val){
                dummy = dummy.next;
            }
            ptr.next = dummy;
            ptr = ptr.next;
        }
            
        return ans.next;
    }
}