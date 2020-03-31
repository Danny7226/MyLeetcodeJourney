/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null){
            return null;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode ans = dummy, prev = dummy;
        dummy = dummy.next;
        while (dummy != null){
            if (dummy.next != null && dummy.next.val == dummy.val){
                while (dummy.next != null && dummy.next.val == dummy.val){
                    dummy = dummy.next;
                }
                dummy = dummy.next;
                prev.next = dummy;
            }
            else{
                prev = prev.next;
                dummy = dummy.next;
            }
        }
        return ans.next;
    }
}