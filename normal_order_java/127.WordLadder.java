class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Map<String, List<String>> dict = new HashMap<>();
        for(String word: wordList){
            char[] cur = word.toCharArray();
            for(int i = 0; i < cur.length; i++){
                char prev = cur[i];
                cur[i] = '*';
                String toAdd = new String(cur);
                // System.out.println(toAdd);
                if(!dict.containsKey(toAdd)){
                    dict.put(toAdd, new ArrayList<String>());
                }
                dict.get(toAdd).add(word);
                cur[i] = prev;
            }
        }
        // System.out.println(dict.get("*ot"));
        Set<String> seen = new HashSet<>();
        Queue<String[]> q = new LinkedList<>();
        q.offer(new String[]{beginWord, "1"});
        int range, ans;
        while(!q.isEmpty()){
            range = q.size();
            for(int i = 0; i < range; i++){
                String[] cur = q.poll();
                ans = Integer.valueOf(cur[1]);
                char[] curWord = cur[0].toCharArray();
                int size = cur[0].length();
                for(int j = 0; j < size; j++){
                    char prev = curWord[j];
                    curWord[j] = '*';
                    String toAdd = new String(curWord);
                    // System.out.println(toAdd);
                    for(int k = 0; k < dict.getOrDefault(toAdd, new ArrayList<String>()).size(); k++){
                        String tmp = dict.get(toAdd).get(k);
                        if(tmp.equals(endWord)) return ans+1;
                        if(!seen.contains(tmp)){
                            seen.add(tmp);
                            q.offer(new String[]{tmp, String.valueOf(ans+1)});
                        }
                    }
                    curWord[j] = prev;
                }
            }
        }
        return 0;
    }
}