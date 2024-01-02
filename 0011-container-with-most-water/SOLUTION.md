## Intuition
We need to find the container with the most water. In this context, a container is made by two lines, each line represented by the element at the chosen index in the input array. Now:

> **Water held by a container = length * height**

let the indices be `i` and `j`.

`length` will be the difference between the indices of the two lines. 
`height` equals the limiting height, i.e. the lesser of the two elements at indices `i` and `j`. 

This intuitively means that we need to use a two pointer approach.
<!-- Describe your first thoughts on how to solve this problem. -->

## Approach

1. Initialize pointers `start` and `end` at the beginning and end of the array `height`.
2. Initialize `max` to -1, representing the maximum area.
3. While `start` is less than `end`:
    - Retrieve the heights of the lines at positions `start` and `end` (`s` and `e`).
    - Calculate the current area using the formula `Math.abs(end - start) * Math.min(s, e)`.
    - Update `max` with the maximum of the current area and the previous maximum.
    - If the height at `start` is less than the height at `end`, increment `start` until a greater or equal height is found.
    - If the height at `end` is less than or equal to the height at `start`, decrement `end` until a greater height is found.
4. Return the final maximum area.
<!-- Describe your approach to solving the problem. -->

-x-x-x-

### Why do we update `start` and `end` the way we do?

When we increment start or decrement end, we do so by checking which of the two heights is lesser. This is because that height is the limiting factor. To find areas that are larger than the current area, we need to find greater elements at start and end indices. 

Hence, we increment start if `height[start] < height[end]` (height at start is the limiting element), and vice versa. 

We also continually update start and end while the heights at the updated indices are less than the originals. This is because as the distance between the two lines is decreasing, having the same heights or lesser at the updated indices will never yield a bigger area. We only calculate the area and update `maxArea` if there is a chance at a highter area, which is only possible when the new start or end heights are greater than the originals. 

# Complexity
- Time complexity: $O(n)$
    We only go over the aray once using the two pointer approach, and each iteration has constant time functions.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
    We only declare some constant space variables (start, end, s, e, max). 
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution {
    public int maxArea(int[] height) {
        int start = 0;
        int end = height.length - 1;
        int max = -1;

        while(start < end) {
            int s = height[start];
            int e = height[end];
            max = Math.max(Math.abs(end - start) * Math.min(s,e), max);
            if(s < e){
                while(start < end && height[start] <= s) start++;
            } else {
                while(start < end && height[end] <= e)end--;
            }
        }

        return max;
    }
}
```