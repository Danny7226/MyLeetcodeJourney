/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public boolean isPalindrome(ListNode head) {
        List<ListNode> ll = new ArrayList<ListNode>();
        while (head!=null){
            ll.add(head);
            head = head.next;
        }
        ListNode a[] = ll.toArray(new ListNode[ll.size()]);
        // System.out.println(a);
        int j = a.length - 1;
        for(int i = 0; i < a.length; i++){
            if (a[i].val != a[j].val){
                return false;
            }
            j--;
        }
        return true;
    }
}

class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode l1 = head;
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // reverse 2nd half linked list
        ListNode rev = null;
        while (slow != null){
            ListNode tmp = rev;
            rev = slow;
            slow = slow.next;
            rev.next = tmp;
        }

        // check palindrome
        while (rev != null){
            if (rev.val != l1.val){
                return false;
            }
            rev = rev.next;
            l1 = l1.next;
        }
        return true;
        
    }
}