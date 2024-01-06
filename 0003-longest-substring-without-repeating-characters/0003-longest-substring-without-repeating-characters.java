class Solution {
    public int lengthOfLongestSubstring(String s) {
        int len = s.length();
        if(len <= 1) return len;

        Set<Character> set = new HashSet();

        int start = 0;
        int end = 0;

        int max = 0;

        while(end < len) {
            Character c = Character.valueOf(s.charAt(end));
            if(set.add(c)) {
                end++;
            } else {
                max = Math.max(max, end-start);
                while(set.contains(c)) {
                    set.remove(Character.valueOf(s.charAt(start)));
                    start++;
                }
            }

            if(end == len) {
                max = Math.max(max, end-start);
            }
        }

        return max;
    }
}