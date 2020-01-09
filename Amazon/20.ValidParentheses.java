class Solution {
    HashSet<Character> set = new HashSet<>();
    Map<Character, Character> pair = new HashMap<>();    
    Solution(){
        set.add('[');
        set.add('{');
        set.add('(');
        pair.put('}','{');
        pair.put(']','[');
        pair.put(')','(');        
    }
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i<s.length(); i++){
            char cur = s.charAt(i);
            if(set.contains(cur)) stack.push(cur);
            else{
                if(stack.isEmpty() || stack.pop() != pair.get(cur)) return false;
            }
        }
        return stack.isEmpty();
    }
}