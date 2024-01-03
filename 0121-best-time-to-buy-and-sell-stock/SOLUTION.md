# Intuition
The logic behind this problem is that we treat each element as a potential selling day. To achieve the maximum profit, we calculate the difference between the price that day and the minimum price till then. Hence, the most efficient solution to this problem involve tracking just two variables while iterating over the array: `min_price` and `max_profit`.



# Approach
1. Initialize `max_profit` and `min_price`.
2. Iterate over the input array:
    - For each price in the array, we update:
        - min_price as the minimum of min_price and the current price
        - max_profit as the maximum of max_profit and maximim profit if we sold the stocks this day (`price - min-price`).
3. Return `max_profit` at the end of the loop.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: O(n)
This algorithm goes over each element only once, executing constant time operations for each element.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
This approach only uses constant size variables for auxiliary space. 
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
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
```