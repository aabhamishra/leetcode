class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0, min_price = Integer.MAX_VALUE;
        
        for(int price : prices) {
            min_price = Math.min(min_price, price);
            max_profit = Math.max(max_profit, price-min_price);
        }

        return max_profit;
    }
}
