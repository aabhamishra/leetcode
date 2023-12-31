class Solution {
    public String removeDigit(String number, char digit) {
        int last_index = 0;
        int len = number.length();

        for(int i = 1; i < len; i++) {
            if(number.charAt(i-1) == digit) {
                if(number.charAt(i) > digit) {
                    return number.substring(0,i-1) + number.substring(i, len);
                }
                last_index = i-1;
            }
        }

        if(number.charAt(len - 1) == digit) last_index = len - 1;

        return number.substring(0,last_index) + number.substring(last_index+1, len);
    }
}