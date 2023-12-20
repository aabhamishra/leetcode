class Solution {
    public boolean isAnagram(String s, String t) {
        
        int len = s.length();
        if(len != t.length()) return false;
        
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        
        Arrays.sort(sArr);
        Arrays.sort(tArr);
        
        for(int i = 0; i < len; i++) {
            if(sArr[i] != tArr[i]) return false;
        }
        
        return true;
    }
    
}