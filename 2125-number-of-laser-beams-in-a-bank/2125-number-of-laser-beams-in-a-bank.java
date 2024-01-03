class Solution {
    public int numberOfBeams(String[] bank) {

        int m = bank.length;
        if(m == 1) return 0;

        int n = bank[0].length();

        int beams = 0, prev = 0;

        for(String row : bank ){
            int curr = 0;

            for(int j = 0; j < n; j++) {
                if(row.charAt(j) == '1') curr++;
            }

            if(curr != 0) {
                beams += prev*curr;
                prev = curr;
            }
        }
        return beams;
    }
}