class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int diff = 0;

        for( int i = 1; i < prices.length; i++) {
            diff = prices[i] - prices[i-1];
            if(diff > 0) {
                max += diff;       
            }
        }

        return max;
    }                               
}