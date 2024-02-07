## Intuition

The algorithm constructs a custom sorted string by first creating a frequency map of characters in the input string `s`. Then, it iterates through the order string `order` to append the characters in the desired order, followed by any remaining characters not present in the order string.

## Approach
1. It initializes an empty dictionary `map`.

2. It iterates through each character in the string `s`. For each character, it updates the dictionary `map` such that the key is the character and the value is the concatenation of the character with itself (to keep track of the frequency of characters in the original string).
3.   It re-initializes `s` as `""` to store the result.
4.   It iterates through each character in the `order` string. For each character, if it exists in the `map`, it appends the concatenated string corresponding to that character to `s` and removes the character from the `map`.
5.   After the above loop, there might be characters left in the `map` (characters from `s` that are not in the `order`). It iterates through these remaining characters and appends their concatenated strings to `s`.
6.   Finally, it returns the sorted string `s`.

## Complexity
- Time complexity:
The time complexity is O(N + M), where N is the length of the input string `s` and M is the length of the order string `order`. The algorithm iterates through each character of the input string `s` to create the frequency map and through each character of the order string `order`.

- Space complexity:
The space complexity is O(N), where N is the length of the input string `s`. The algorithm uses additional space for the frequency map.

## Code
```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map = {}

        for c in s:
            map[c] = map.get(c, "") + c
        
        s = ""

        for c in order:
            if c in map:
                s += map[c]
                del map[c]
        
        for left_char in map:
            s += map[left_char]
        
        return s
```