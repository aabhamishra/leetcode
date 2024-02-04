class Solution {
    int[] prefix;
    int len;
    public Solution(int[] w) {
        // array of prefix sums
        len = w.length;
        prefix = new int[len];
        prefix[0] = w[0];
        for(int i = 1; i < len; i++) {
            prefix[i] = prefix[i-1] + w[i];
        }
    }
    
    public int pickIndex() {
        Random r = new Random();
        return binarySearch(r.nextInt(prefix[len-1]) + 1);
    }

    private int binarySearch(int num) {
        int start = 0, end = len - 1;

        while(start < end){
            int mid = start + (end-start)/2;

            if(prefix[mid] < num) {
                start = mid+1;
            } else {
                end = mid;
            }
        }

        return start;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */