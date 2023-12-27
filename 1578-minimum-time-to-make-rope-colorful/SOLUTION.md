## Logistics
Attempt date: 27 December 2023
|| Runtime: 8 ms ( beat 90% of other submissions ) || Memory: 60 MB


## Intuition
The problem requires us to find the minimum time Bob needs to make the rope colorful by removing some balloons. The condition is that no two consecutive balloons should have the same color. We are given the colors of balloons and the time needed to remove each balloon. To minimize the time, we need to strategically choose which balloons to remove. The given solution uses a two-pointer approach to iterate through the string of colors and determine the minimum time needed to make the rope colorful.


## Approach
1. Initialize three pointers: `first` and `second` to iterate through the string of colors, and `i` to keep track of the step size for the `first` pointer.
2. Use a while loop to iterate through the string until both pointers are within the bounds.
3. Check if the colors of balloons at the `first` and `second` pointers are the same.
   - If they are the same, compare the needed time for both balloons.
      - If the time needed for the balloon at the `first` pointer is less than or equal to the time needed for the balloon at the `second` pointer:
         - Increment the total time by the needed time for the balloon at the `first` pointer.
         - Move the `first` pointer to the next non-consecutive balloon (skip `i` balloons).
         - Reset the step size `i` to 1.
         - Increment the `second` pointer.
      - If the time needed for the balloon at the `second` pointer is less:
         - Increment the total time by the needed time for the balloon at the `second` pointer.
         - Increment the step size `i`.
         - Increment the `second` pointer.
   - If the colors are different, move both pointers to the next non-consecutive balloon.
4. Continue this process until both pointers are within the bounds.
5. Return the total time, which represents the minimum time needed to make the rope colorful.

## Complexity Analysis
- **Time Complexity:** O(n), where n is the length of the input string `colors`. The algorithm iterates through the string once using two pointers.
- **Space Complexity:** O(1), as the algorithm uses a constant amount of space for the pointers and variables. It does not use any additional data structures that scale with the input size.

```java
class Solution {
    public int minCost(String colors, int[] neededTime) {
        int time = 0;
        int first = 0;
        int second = 1;
        int len = colors.length();
        int i = 1;
        
        while (first < len && second < len) {
            if (colors.charAt(first) == colors.charAt(second)) {
                if (neededTime[first] <= neededTime[second]) {
                    time += neededTime[first];
                    first += i;
                    i = 1;
                    second++;
                } else {
                    time += neededTime[second];
                    i++;
                    second++;
                }
            } else {
                first += i;
                i = 1;
                second++;
            }
        }

        return time;
    }
}
