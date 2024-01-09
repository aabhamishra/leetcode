# [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window**  <div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:rc:">**substring** <div style="position: fixed; z-index: 40; inset: 0px auto auto 0px; transform: translate(646px, 222px);"> of `s` such that every character in `t` (**including duplicates** ) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is **unique** .

**Example 1:** 

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:** 

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:** 

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

**Constraints:** 

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

**Follow up:**  Could you find an algorithm that runs in `O(m + n)` time?