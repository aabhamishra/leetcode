## Intuition
To find the most optimized solution, let's first think of the brute force approach. That will involve taking each temperature into consideration, and iterating till we find the next highest temperature. We then record the difference between the two indices. 

Howevever, this approach can involve going over each element multiple times, which is not optimal. 

The optimzied algorithm utilizes a stack to efficiently compute the number of days one needs to wait until a warmer temperature for each day in the input array `temp`. It initializes an array `res` to store the results, where each element initially holds the value 0. Additionally, an empty stack is employed to keep track of indices in the `temp` array for which a future day with a higher temperature is yet to be found.

## Approach
The algorithm iterates through the `temp` array, using a loop to process each day's temperature. For each day, it checks whether the stack is not empty and if the temperature at the current index is greater than the temperature at the index stored at the top of the stack. If these conditions are met, it means that a warmer day has been found, and the algorithm updates the result for the index at the top of the stack, then pops that index from the stack. This process continues until the stack is empty or the condition is not satisfied. Finally, the current index is pushed onto the stack.

By the end of the iteration, the `res` array holds the number of days one must wait until a warmer temperature for each corresponding day in the input array `temp`.

## Complexity
- Time complexity: $O(N)$
The time complexity is O(N), where N is the length of the input array `temp`. The algorithm iterates through the array once, and each element is pushed and popped from the stack at most once.

- Space complexity: $O(N)$
The space complexity is O(N), where N is the length of the input array `temp`. In the worst case, the stack could contain all elements of the array.

## Code
```python
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = []

        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return res

```