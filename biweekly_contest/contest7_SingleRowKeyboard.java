class Solution {
    public int calculateTime(String keyboard, String word) {
        Map<Character, Integer> hm = new HashMap<>();
        for(int i = 0; i < keyboard.length(); i++){
            hm.put(keyboard.charAt(i), i);
        }
        int ans = 0, prev = 0;
        for(int i = 0; i < word.length(); i++){
            ans += Math.abs(hm.get(word.charAt(i)) - prev);
            prev = hm.get(word.charAt(i));
        }
        return ans;
    }
}