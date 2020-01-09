/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // merge sort O(NlogK), space O(1)
        if(lists.length == 0) return null;
        return partition(lists, 0, lists.length-1);
    }
    
    public ListNode partition(ListNode[] lists, int from, int to){
        if(from == to) return lists[from];
        int mid = from + (to - from) / 2;
        ListNode l1 = partition(lists, from, mid);
        ListNode l2 = partition(lists, mid+1, to);
        return merge(l1, l2);
    }
    
    public ListNode merge(ListNode node1, ListNode node2){
        if(node1 == null) return node2;
        if(node2 == null) return node1;
        if(node1.val <= node2.val){
            node1.next = merge(node1.next, node2);
            return node1;
        } else{
            node2.next = merge(node2.next, node1);
            return node2;
        }
    }
}
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // heap O(NlogK), where k denotes number of lists;, space O(K)
        PriorityQueue<ListNode> pq = new PriorityQueue<>(new Comparator<ListNode>(){
            @Override
            public int compare(ListNode node1, ListNode node2){
                if(node1.val == node2.val) return 0;
                else if(node1.val < node2.val) return -1;
                else return 1;
            }
        });
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for(ListNode node: lists){
            if(node!=null) pq.offer(node);
        }
        while(!pq.isEmpty()){
            ListNode temp = pq.poll();
            cur.next = temp;
            cur = cur.next;
            if(temp.next != null) pq.offer(temp.next);
        }
        return dummy.next;
    }
}