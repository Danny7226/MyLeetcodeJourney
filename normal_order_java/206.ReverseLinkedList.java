class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode rev = null;
        while (head!=null){
        	ListNode tmp = rev;
        	rev = head;
        	head = head.next;
        	rev.next = tmp;
        }
        return rev;
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