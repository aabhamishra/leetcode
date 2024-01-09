# Algorithm Explanation: Minimum Window Substring

## Objective
The algorithm aims to find the minimum window substring of string `s` that contains all the characters of string `t`.

## Intuition
- The algorithm uses a sliding window approach to explore potential substrings in string `s`.
- It maintains two dictionaries, `tMap` and `sMap`, to track the frequency of characters in strings `t` and `s`.
- It increases the right pointer till we have all matches, and then decreases the left pointer to try to reduce the length of the valid window.

## Approach
1. Check if the length of `t` is greater than the length of `s`. If true, return an empty string since it's impossible to have a window containing all characters of `t` in `s`.
2. Initialize variables `res` and `res_len` to represent the minimum window substring and its length. Set `res_len` to a value greater than the length of `s`.
3. Initialize two dictionaries, `tMap` and `sMap`, to store the frequency of characters in strings `t` and `s`.
4. Populate the `tMap` dictionary with the frequency of characters in string `t`.
5. Initialize variables `need`, `l`, `r`, and `count` to keep track of the number of characters needed, left and right pointers, and the count of characters satisfying the conditions.
6. Iterate over the characters in string `s` using the right pointer (`r`):
   - If the current character `s[r]` is in `tMap`, update `sMap` with the frequency of `s[r]`.
   - If the count of `sMap[s[r]]` becomes equal to the count in `tMap[s[r]]`, increment `count` (indicating that a potential window is found).
   - While `count` is equal to `need`:
     - Update the result (`res`) and its length (`res_len`) if the current window is smaller.
     - If `s[l]` is in `sMap`, decrement `sMap[s[l]]`.
     - If the count of `sMap[s[l]]` becomes less than `tMap[s[l]]`, decrement `count` (indicating that the window is no longer valid).
     - Increment the left pointer (`l`) to shrink the window.
7. Return the minimum window substring (`res`).

## Time Complexity $O(n)$
- The algorithm iterates through each character in `s` once. The time complexity is O(N), where N is the length of `s`.

## Space Complexity $O(M)$
- The algorithm uses additional space for two dictionaries (`tMap` and `sMap`) and other variables. The space complexity is O(M), where M is the size of the character set in `t`.

## Code
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        res = ""
        res_len = len(s) + 1
        tMap, sMap = {}, {}

        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        need = len(tMap)
        l, r, count = 0, 0, 0

        for r in range(len(s)):
            if s[r] in tMap:
                sMap[s[r]] = 1 + sMap.get(s[r], 0)
                if sMap[s[r]] == tMap[s[r]]:
                    count += 1

                    while count == need:
                        if r - l + 1 < res_len:
                            res_len = r - l + 1
                            res = s[l:r + 1]

                        if s[l] in sMap:
                            sMap[s[l]] -= 1

                            if sMap[s[l]] < tMap[s[l]]:
                                count -= 1
                        l += 1
        return res
```
