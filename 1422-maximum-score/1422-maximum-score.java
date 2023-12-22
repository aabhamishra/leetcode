class Solution {
    public int maxScore(String s) {
        int max = 0;
        int curr_max = 0;
        int index = 0;

        for(int i = 0; i < s.length() - 1; i++) {
            if(s.charAt(i) == '0') max++;
            else max--; 

            if(max >= curr_max) {
                curr_max = max;
                index = i;
            }
        }

        max = 0;

        for(int i = 0; i <= index; i++){
            if(s.charAt(i) == '0') max++;
        }
        for(int i = index + 1; i < s.length(); i++) {
            if(s.charAt(i) == '1') max++;
        }

        return max;
    }
}