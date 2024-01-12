## Intuition
The algorithm explores all possible combinations of parentheses using a DFS approach. It ensures that the parentheses are balanced by maintaining counts of open and close parentheses. The base case ensures that only valid combinations are added to the result.


## Approach
The algorithm aims to generate all valid combinations of parentheses for a given `n`. It uses a recursive Depth-First Search (DFS) approach to explore all possible combinations. The base case for the recursion is when both the open and close counts reach the target `n`, at which point the current combination is appended to the result.

The DFS function (`dfs`) takes three parameters: `open_count` representing the count of open parentheses, `close_count` representing the count of close parentheses, and `curr` representing the current combination of parentheses.

The algorithm explores two possibilities at each recursive step:
1. If the `open_count` is less than `n`, it adds an open parenthesis to the current combination and makes a recursive call with incremented `open_count`.
2. If the `close_count` is less than `open_count`, it adds a close parenthesis to the current combination and makes a recursive call with incremented `close_count`.

## Complexity
- Time complexity: $O(2^n)$
The time complexity is determined by the number of recursive calls made. At each step, the algorithm makes two recursive calls, leading to a time complexity of O(2^N), where N is the given input `n`.

- Space complexity: $O(n)$
The space complexity is primarily influenced by the depth of the recursion stack. In the worst case, the maximum depth of the recursion is `2n` (when both open and close counts reach `n`). Therefore, the space complexity is O(2N), where N is the given input `n`.

## Code
```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack = []
        res = []

        def dfs(open_count: int, close_count: int, curr: str):
            if open_count == close_count == n:
                res.append(curr)
                return
            
            if open_count < n:
                dfs(open_count+1, close_count, curr+"(")
            
            if close_count < open_count:
                dfs(open_count, close_count+1, curr+")")
        
        dfs(0,0,"")
        return res
        
            
```