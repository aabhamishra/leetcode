class Solution {
    public boolean winnerOfGame(String colors) {
        int A = 0;
        int B = 0;
        int curr = 0;
        boolean isA = false;
        
        for( int i = 0; i < colors.length(); i++) {
            char c = colors.charAt(i);

            if(c == 'A') {
                if(isA) curr++;
                else {
                    if(curr >= 3) B += curr - 2; 
                    curr = 1;
                    isA = true;
                }
            } else {
                if(!isA) {
                    if(curr >= 3) A += curr - 2;
                    curr = 1;
                    isA = false;
                }
                else curr++;
            }    
        }

        if(curr >= 3) {
            if(isA) A+= curr - 2;
            else B += curr - 2;
        } 

        if(A > B) return true;
        
        return false;
    }
}