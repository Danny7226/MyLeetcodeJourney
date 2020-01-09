class Node{
    Node next;
    Node prev;
    int val;
    int key;
    Node(int key, int val){
        this.val = val;
        this.key = key;
    }
}
class DoubleLinkedList{
    Node head;
    Node tail;
    DoubleLinkedList(){
        head = new Node(0,0);
        tail = new Node(0,0);
        head.next = tail;
        tail.prev = head;
    }
    public void moveToFront(Node node){
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev;
        
        addNode(node);
    }
    public void addNode(Node node){
        // always add node after dummy head;
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;        
    }
    public Node cutTail(){
        Node node = tail.prev;
        node.prev.next = node.next;
        node.next.prev= node.prev;
        return node;
    }
    
}

class LRUCache {
    //One advantage of double linked list is that the node can remove itself without other reference. In addition, it takes constant time to add and remove nodes from the head or tail.
    Map<Integer, Node> cache;
    DoubleLinkedList dll;
    int size;
    int capacity;
    public LRUCache(int capacity) {
        size = 0;
        this.capacity = capacity;
        cache = new HashMap<>();
        dll = new DoubleLinkedList();
    }
    
    public int get(int key) {
        if(cache.containsKey(key)){
            Node node = cache.get(key);
            dll.moveToFront(node);
            return node.val;
        }
        else return -1;
    }
    
    public void put(int key, int value) {
        if(cache.containsKey(key)){
            Node node = cache.get(key);
            node.val = value;
            dll.moveToFront(node);
        }else{
            Node node = new Node(key, value);
            cache.put(key, node);
            dll.addNode(node);
            size++;
            if(size>capacity){
                int drop = dll.cutTail().key;
                cache.remove(drop);
                size--;
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */


// class LRUCache {
//     private int capacity;
//     Map<Integer, Integer> hm;
//     LinkedList<Integer> lru;
//     public LRUCache(int capacity) {
//         this.capacity = capacity;
//         lru = new LinkedList<>();
//         hm = new HashMap<>();
//     }
    
//     public int get(int key) {
//         if(hm.containsKey(key)) {
//             lru.removeFirstOccurrence(key); //O(N)
//             lru.add(key);
//             return hm.get(key);  
//         }
//         else return -1;
//     }
    
//     public void put(int key, int value) {
//         if(hm.containsKey(key)){
//             hm.put(key, value);
//             lru.removeFirstOccurrence(key);
//             lru.add(key);
//         } else{
//             lru.add(key);
//             if(lru.size() > capacity){
//                 int first = lru.removeFirst();   
//                 hm.remove(first);
//             }
//             hm.put(key, value);
//         }
//     }
// }

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */