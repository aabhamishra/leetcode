# Intuition
The algorithm uses two arrays to keep track of the frequency of characters in `s1` and the current window of characters in `s2`.

The `count` variable keeps track of the number of characters with matching frequencies in `s1` and `s2`.

The algorithm iterates over `s2`, updating the window's frequency arrays and `count`. If `count` reaches 26, a permutation of `s1` is found in the substring.

# Approach
1. Check if the length of `s1` is greater than the length of `s2`. If true, return `false` since `s1` cannot be a substring of `s2`.
2. Initialize two arrays `s1map` and `s2map` of size 26 to represent the frequency of characters in `s1` and `s2`.
3. Populate the frequency arrays `s1map` and `s2map` for the first `s1.length()` characters in `s1` and `s2`.
4. Initialize a variable `count` to 0 and increment it for each character where `s1map[i] == s2map[i]`.
5. Iterate over the remaining characters in `s2` starting from index `s1.length()`:
   - Update the frequency arrays `s2map` based on the left and right pointers in this window.
   - Return true if `count` equals 26 i.e. all characters are matched.
   - For each pointer, check if adding (in case of r) or removing (in case of l) that character has any effect on count. If so, update count:
        - If the new frequencies equal, increment count
        - If the new frequencies get mismatched but were equal before, decrement count.
6. Return `true` if `count` is equal to 26; otherwise, return `false`.

# Complexity
- Time complexity: $O(n)$
The algorithm iterates through both strings once, performing constant-time operations for each character. The time complexity is O(N), where N is the length of the longer string (`s2`).

- Space complexity: $O(1)$
The algorithm uses additional space for two arrays (`s1map` and `s2map`) and other variables. The space complexity is O(1) since the character set is constant.


# Code
```
public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length())
            return false;
        int[] s1map = new int[26];
        int[] s2map = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            s1map[s1.charAt(i) - 'a']++;
            s2map[s2.charAt(i) - 'a']++;
        }

        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (s1map[i] == s2map[i])
                count++;
        }

        for (int i = 0; i < s2.length() - s1.length(); i++) {
            int r = s2.charAt(i + s1.length()) - 'a', l = s2.charAt(i) - 'a';
            if (count == 26)
                return true;
            s2map[r]++;
            if (s2map[r] == s1map[r]) {
                count++;
            } else if (s2map[r] == s1map[r] + 1) {
                count--;
            }
            s2map[l]--;
            if (s2map[l] == s1map[l]) {
                count++;
            } else if (s2map[l] == s1map[l] - 1) {
                count--;
            }
        }
        return count == 26;
    }
}
```