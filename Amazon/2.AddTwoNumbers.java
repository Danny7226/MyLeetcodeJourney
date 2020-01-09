/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0, digit = 0;
        ListNode ans = new ListNode(0);
        ListNode res = ans;
        while(l1 != null && l2 != null){
            if(carry + l1.val + l2.val > 9){
                digit = carry + l1.val + l2.val - 10;
                carry = 1;
            }else{
                digit = carry + l1.val + l2.val;
                carry = 0; 
            }
            ans.next = new ListNode(digit); 
            ans = ans.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        while(l1 != null){
            if(carry + l1.val > 9){
                digit = carry + l1.val - 10;
                carry = 1;
            }else{
                digit = carry + l1.val;
                carry = 0;
            }
            ans.next = new ListNode(digit); 
            ans = ans.next;
            l1 = l1.next;
        }
        while(l2 != null){
            if(carry + l2.val > 9){
                digit = carry + l2.val - 10;
                carry = 1;
            }else{
                digit = carry + l2.val;
                carry = 0;
            }
            ans.next = new ListNode(digit); 
            ans = ans.next;
            l2 = l2.next;           
        }
        if(carry == 1) ans.next = new ListNode(1);
        return res.next;
    }
}