## Intuition
In the brute force approach, we go ovwr each window, find the greatest element, and add it to the result array.

However, this can be very time consuming. The point behind the optimized problem is to maintain an always decreasing list of elements in the current window. This can be done in Python using a deque: an optimized list supporting efficient insertiins and deletioins from the start and end.

In the context of this problem, we maintain a deque listing the indices associated with elements in the decreasing order. The highest elements are always at the front ( index 0 ) for efficient retrival. As the sliding window moves as a new element is incorporated, two things happen:

1. We compare the elements in the queue (starting on the right - index -1) with the element to insert. While the element associated with index at -1 in the deque is smaller than the current element, we`pop()` the deque. We finally insert the current element.

2. If the list contains an element that is no longer in the window (we match the left pointer with the first element of the deque), we `popleft()`.

These operations guarantee that the element being added top the result array is the highest element in the sliding window. 
<!-- Describe your first thoughts on how to solve this problem. -->

## Approach
1. Initialize an empty list `res` to store the maximum elements in each window.
2. Initialize a deque (`queue`) to store indices of elements in the current window.
3. Initialize pointers `l` and `r` to represent the left and right boundaries of the current window.
4. Iterate through the array `nums` using the right pointer (`r`):
   - While the deque is not empty and the element at the back of the deque (`nums[queue[-1]]`) is smaller than the current element (`nums[r]`), pop elements from the back of the deque. This ensures that the deque stores only potential maximum elements for the current window.
   - Add the current index `r` to the deque.
   - If the index at the front of the deque (`queue[0]`) is outside the current window (`l > queue[0]`), pop the front element from the deque.
   - If the window is valid (`r + 1 >= k`), add the maximum element in the current window (`nums[queue[0]]`) to the result (`res`) and increment the left pointer (`l`).
   - Increment the right pointer (`r`).
5. Return the list of maximum elements in each sliding window (`res`).


## Complexity
- Time complexity: $O(n)$
The algorithm iterates through each element in `nums` once. The time complexity is O(N), where N is the length of `nums`.

- Space complexity: $O(n)$
The algorithm uses additional space for the deque (`queue`) and the result list (`res`). The space complexity is O(N), where N is the length of `nums`.


## Code
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = collections.deque()
        l, r = 0, 0

        while r < len(nums):
            # pop smaller than current values. use WHILE!!!
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            # add current value
            queue.append(r)

            # pop left index if exists
            if l > queue[0]:
                queue.popleft()

            # add to result when window is valid
            if r+1 >= k:
                res.append(nums[queue[0]])
                l+=1

            # increse right pointer 
            r+=1
        
        return res
            
```