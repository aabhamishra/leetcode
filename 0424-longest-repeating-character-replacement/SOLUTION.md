## Intuition
The brute force way of solving this proiblem is to consider every possible substring of `s`, and finding the longest *valid* substring. By *valid*, we mean that the substring should have consecutive characters after replacing at most `k` characters. 

In any substring, it is better to keep the character that occurs most frequently, as replacing the rest of the characters will require less operations.

e.g. In this substring `ABABBX`, we have `B` as the most frequent character. We can notice that keeping the `B`s and replacing the `A` and `X` requires the least number of replacements.

Now, in our optimized solution, instead of checking every substring (which will take $O(n^2)$ time), we maintain a window with two pointers, and a hashmap for character frequencies in tha window.

This approach tracks the maximum length of a valid window. We increase the right pointer to lengthen the window as long as the window is valid. We check for validity by verifying that the most needed character replacements `(length of window - max frequency of a character)`are `<=k`. 

Now, when a window is no longer valid, we start to increase the left pointer. This will decrease the window till it is valid again.

During both pointer movements, we also update out hashmap which maps the character to its frequency in the window. Additionally, we keep track of the maximum frequency in the window so that we dont have to traverse the entire hashmap during every iteration to find it.

The algorithm continuously expands and contracts this window to find the longest possible length that is valid. That is our return value.

## Approach

1. Initialize a dictionary `count` to track the frequency of characters in the current window.
2. Initialize variables `max_freq` to track the maximum frequency of any character in the current window.
3. Initialize pointers `l`, `r`, and `res` to 0.
   - `l` and `r` represent the left and right boundaries of the current window.
   - `res` represents the length of the longest valid substring.
4. Iterate through the string using the `r` pointer:
   - Update the count of the character at index `r` in the `count` dictionary.
   - Update `max_freq` with the maximum frequency of any character in the current window.
   - While the condition `(r - l + 1) - max_freq > k` is violated:
     - Decrement the count of the character at index `l`.
     - Increment `l` to shrink the window.
   - Update `res` with the maximum length of a valid substring.
   - Increment `r` to expand the window.
5. Return the length of the longest valid substring (`res`).

## Complexity
- Time complexity: $O(n)$
Both pointers iterate over each element at max once. During each iteration, we perform constant time functions. 
- Space complexity: $O(1)$
We need a 26 entry dictionary at max, as we are only representing upper case letters in the english alphabet. Hence, for larger input strings, the auxiliary space needed becomes O(1). 

## Code
```
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        # maximum frequency character in the hashmap
        max_freq = 0
        l, r, res = 0, 0, 0
        
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            while l <= r and (r-l+1) - max_freq > k:
                count[s[l]] -= 1
                l+=1
        
            res = max(res, r-l+1)
            r+=1

        return res
```