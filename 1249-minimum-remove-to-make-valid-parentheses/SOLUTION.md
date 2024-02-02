## Intuition
If a question involves parentheses, we have to keep the order of appearance in mind. For valid parentheses, all `(` must be matched with a `)` parenthesis. Additionally, a closing parentheses `)` is not valid if there is no `(` before it.

Keeping these restraints in mind, an optimal soltion involves keeping track of parentheses indices in a stack. 

We iterate over the string, adding and removing from the stack every time we encounter either `(` or `)`
<!-- Describe your first thoughts on how to solve this problem. -->

## Approach
<!-- Describe your approach to solving the problem. -->
1. Convert the input string to an array of characters called `chars`.
2. Initialize an empty stack `stack`
3. Iterate over the indices of `chars` using counter `i`. There are two possibilities we need to account for:
    i. If `chars[i]` equals `(`, we have found an open parentheses. We add `i` to the stack.
    ii. Else if `chars[i]` equals `)`, we have found a closing bracket. There are two sub-possibilities in this case:
    - The stack is empty: this means our `)` does not have any matching `(` before it in `chars`. This parenthesis needs to be removed. We mark `chars[i]` as an empty string `""`.
    - The stack is not empty: this means we have a hanging `(` to math our `)`! We pop from the stack and move on as we dont need to remove either of the parentheses. 

4. Finally, we might have some hanging `(` left in `stack`. For each index in the stack, we pop it and mark `chars[i]` as `""`.

At this point, we have *removed* all invalid parentheses from out character array. All we need to do now is to return the string made from concatenating each character in `chars`.

5. Return the string made by concatenating all characters in `chars`. In python, we can use `"".join(chars)`. In Java, use `new String(chars)`.


## Complexity
- Time complexity: $O(N)$
We iterate over the characters only once. All operations are O(1) for each iteration. 
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(N)$
`chars` takes up O(N) space. `stack` will take up at most O(o) space where o is the number of open parentheses in the input string. 

<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        # tracks indices of extra open parentheses
        stack = []

        for i in range(len(chars)):
            if chars[i] == "(":
                stack.append(i)
            elif chars[i] == ")":
                if stack:
                    stack.pop()
                else:
                    chars[i] = ""
        
        while stack:
            chars[stack.pop()] = ""

        return "".join(chars)
        
```