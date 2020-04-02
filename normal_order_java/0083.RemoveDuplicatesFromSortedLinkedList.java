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
        if(head == null) return null;
        ListNode prev = head, cur = head;
        cur = cur.next;
        while(cur!=null){
            if(cur.val == prev.val){
                prev.next = cur.next;
            }
            else prev = cur;
            cur = cur.next;
        }
        
        return head;
    }
}

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null){
            return null;
        }
        ListNode ans = head;
        while (head.next != null){
            if (head.val == head.next.val){
                head.next = head.next.next;
            }
            else{
                head = head.next;
            }
        }
        return ans;
    }
}