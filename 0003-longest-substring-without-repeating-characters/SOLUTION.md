## Intuition
- The algorithm uses a sliding window approach to traverse the string.
- It maintains a HashSet to keep track of unique characters in the current substring.
- The `start` and `end` indices represent the bounds of the current substring.
- By iterating through the string and adjusting the window, the algorithm identifies the longest substring without repeating characters.

## Approach
1. Initialize variables:
   - `len` represents the length of the input string.
   - If `len` is less than or equal to 1, return `len` since a substring with one or zero characters has no repeats.
   - Use a HashSet `set` to track unique characters in the current substring.
   - `start` and `end` represent the indices of the current substring.
   - `max` represents the maximum length of a substring without repeating characters.
2. Iterate through the string:
   - At each step, check if the character at the current `end` index is not in the `set`.
     - If true, add the character to the `set` and increment `end`.
     - If false, update `max` with the maximum of its current value and the length of the current substring (`end - start`).
       - Additionally, move the `start` index to the right until the duplicate character is no longer in the `set`.
   - If `end` reaches the end of the string, update `max` with the length of the current substring.
3. Return the maximum length of a substring without repeating characters (`max`).

## Time Complexity
- The algorithm iterates through the string once using the sliding window approach. The time complexity is O(N), where N is the length of the input string.

**Space Complexity:**
- The algorithm uses additional space for the HashSet (`set`) and other variables. The space complexity is O(min(N, M)), where M is the size of the character set.

## Implementation
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int len = s.length();
        if (len <= 1) return len;

        Set<Character> set = new HashSet();

        int start = 0;
        int end = 0;

        int max = 0;

        while (end < len) {
            Character c = Character.valueOf(s.charAt(end));

            if (set.add(c)) {
                end++;
            } else {
                max = Math.max(max, end - start);

                while (set.contains(c)) {
                    set.remove(Character.valueOf(s.charAt(start)));
                    start++;
                }
            }

            if (end == len) {
                max 
