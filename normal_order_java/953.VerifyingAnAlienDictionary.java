class Solution {
    private int[] priority;
    public boolean isAlienSorted(String[] words, String order) {
        priority = new int[26];
        for(int i = 0; i < order.length(); i++){
            priority[order.charAt(i) - 'a'] = i;
        }
        for(int i = 1; i < words.length; i++){
            if(!isGreater(words[i], words[i-1])) return false;
        }
        return true;
    }
    
    private boolean isGreater(String s1, String s2){
        int i = 0;
        for(i = 0; i < Math.min(s1.length(), s2.length()); i++){
            int cmp = priority[s1.charAt(i) - 'a'] - priority[s2.charAt(i) - 'a'];
            if(cmp > 0) return true; // s1 is greater than s2 at index i
            else if(cmp < 0) return false; // s1 is smaller than s2
            else continue;
        }
        if(s2.length() > i) return false;
        return true;
    }
}