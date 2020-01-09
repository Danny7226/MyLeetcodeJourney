class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs, new CustomComparator());
        return logs;
    }    
}
class CustomComparator implements Comparator<String>{
    public int compare(String log1, String log2){
        String[] s1 = log1.split(" ", 2);
        String[] s2 = log2.split(" ", 2);
        boolean isDigit1 = Character.isDigit(s1[1].charAt(0));
        boolean isDigit2 = Character.isDigit(s2[1].charAt(0));
        if(!isDigit1 && !isDigit2){
            int ans = s1[1].compareTo(s2[1]);
            return ans != 0? ans: s1[0].compareTo(s2[0]);
        } else if(!isDigit1 && isDigit2){
            return -1;
        } else if(isDigit1 && !isDigit2){
            return 1;
        } else return 0;

    }
}