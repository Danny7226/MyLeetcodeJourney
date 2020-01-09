class RandomizedSet {
    ArrayList<Integer> al;
    Map<Integer, Integer> cache;
    Random rand;
    /** Initialize your data structure here. */
    public RandomizedSet() {
        al = new ArrayList<>();
        cache = new HashMap<>();
        rand = new Random();
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if(cache.containsKey(val)) return false;
        al.add(al.size(), val);
        cache.put(val, al.size()-1);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if(!cache.containsKey(val)) return false;
        int index = cache.get(val);
        // move last element to position index
        al.set(index, al.get(al.size()-1));
        cache.put(al.get(al.size()-1), index);
        al.remove(al.size()-1);
        cache.remove(val);
        return true;
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        return al.get(rand.nextInt(al.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */

class Node{
    int val;
    Node next;
    Node prev;
    Node(int value){
        val = value;
    }
}
class DoubleLinkedList{
    Node dummy;
    Node tail;
    DoubleLinkedList(){
        dummy = new Node(0);
        tail = new Node(0);
        dummy.next = tail;
        tail.prev = dummy;
    }
    public void add(Node node){
        node.prev = tail.prev;
        node.next = tail;
        tail.prev.next = node;
        tail.prev = node;
        
    }
    
    public void remove(Node node){
        node.prev.next = node.next;
    }

}
class RandomizedSet {
    DoubleLinkedList dll;
    Map<Integer, Node> cache;
    int size;
    Random rand;
    /** Initialize your data structure here. */
    public RandomizedSet() {
        size = 0;
        dll = new DoubleLinkedList();
        cache = new HashMap<>();
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if(cache.containsKey(val)) return false;
        Node node = new Node(val);
        cache.put(val, node);
        dll.add(node);
        size++;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if(!cache.containsKey(val)) return false;
        Node node = cache.get(val);
        cache.remove(val);
        dll.remove(node);
        size--;
        return true;
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        rand = new Random();
        int idx = rand.nextInt(size);
        for(int val: cache.keySet()){
            if(idx == 0) return val;
            idx--;
        }
        return -1;
    }
}