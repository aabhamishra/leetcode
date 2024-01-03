## Intuition
- The algorithm leverages the fact that, to maximize the total profit, one can buy and sell stocks multiple times, capitalizing on each price increase.
- By calculating the daily difference in stock prices, the algorithm identifies positive differences as opportunities to gain profit.
- Summing up these positive differences results in the maximum profit achievable through multiple buy-and-sell transactions.

## Approach
1. Initialize variables `max` and `diff` to 0. 
   - `max` represents the maximum profit that can be obtained.
   - `diff` represents the difference in stock prices between consecutive days.
2. Iterate through the array `prices` starting from the second day (`i = 1`).
   - Calculate the difference in stock prices between the current day and the previous day (`diff = prices[i] - prices[i-1]`).
   - If the difference is positive (`diff > 0`), it indicates a potential profit.
     - Add the positive difference to the `max` profit.
3. Return the total maximum profit (`max`).

### Time Complexity
- The algorithm iterates through the array `prices` once, performing constant-time operations. The time complexity is O(N), where N is the length of the array.

### Space Complexity
- The algorithm uses a constant amount of extra space for variables (`max`, `diff`, `i`). The space complexity is O(1).

## Implementation
```java
class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] - prices[i - 1] > 0) {
                max += prices[i] - prices[i - 1];
            }
        }
        return max;
    }
}
```