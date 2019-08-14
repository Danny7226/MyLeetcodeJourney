import java.util.*;
class ListNode{
    int val;
    ListNode next;
    public ListNode(int n){
        val = n;
    }
    public static List print(ListNode head){
        List<Integer> a = new ArrayList<Integer>();
        while(head!=null){
            a.add(head.val);
            head = head.next;
        }
        return a;
    }
}