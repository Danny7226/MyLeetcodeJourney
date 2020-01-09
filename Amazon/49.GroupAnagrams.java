class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> hm = new HashMap<>();
        int[] count = new int[26];
        for(String str: strs){
            Arrays.fill(count, 0);
            // count how many times each letter shows up
            char[] ca = str.toCharArray();
            for(char c: ca)
                count[c - 'a']++;
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < 26; i++){
                sb.append(count[i]);
            }
            String key = sb.toString();
            // System.out.println(key);
            if(hm.containsKey(key)) hm.get(key).add(str);
            else {
                hm.put(key, new ArrayList<>());
                hm.get(key).add(str);
            };
        }
        List<List<String>> ans = new ArrayList<>();
        for(String key: hm.keySet()){
            ans.add(hm.get(key));
        }
        return ans;
    }
}

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList<String>> hm = new HashMap<>();
        for(String str: strs){
            char[] c = str.toCharArray();
            Arrays.sort(c);
            String key = String.valueOf(c);
            if(hm.containsKey(key)) hm.get(key).add(str);
            else{
                hm.put(key, new ArrayList<>());
                hm.get(key).add(str);
            }
        }
        List<List<String>> ans = new ArrayList<>();
        for(String key: hm.keySet()){
            ans.add(hm.get(key));
        }
        return ans;
    }
}