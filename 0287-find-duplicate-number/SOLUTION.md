## Intuition

The given algorithm uses Floyd's Tortoise and Hare algorithm to find the first element in a cycle within a list. The idea is to use two pointers, one moving at a slower pace (tortoise) and the other at a faster pace (hare). If there is a cycle, these pointers will eventually meet at some point within the cycle. After they intersect, another pointer is initialized from the start, and it is moved one step at a time along with the slow pointer. The point where they meet indicates the start of the cycle.

## Approach
1. Initialize two pointers, `slow` and `fast`, both pointing to the first element of the list.
2. Advance `slow` by one step and `fast` by two steps at each iteration until they intersect within the cycle.
3. Once they intersect, break out of the first loop.
4. Initialize another pointer, `slow2`, from the start of the list.
5. Iterate `slow` and `slow2` one step at a time until they meet. The meeting point is the start of the cycle.

## Complexity
- Time complexity: $O(N)$
The time complexity is O(N), where N is the length of the list. This is because the algorithm traverses the list in two phases: finding the intersection point and finding the start of the cycle.

- Space complexity: $O(1)$
The space complexity is O(1) as the algorithm uses only a constant amount of extra space for the pointers.

## Code
```
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # initialize two pointers
        slow = fast = 0

        # advance slow by 1 and fast by 2 wrt index till they intersect
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # init another slow pointer from start
        slow2 = 0

        # iterate till slow and slow2 meet, which will indicate the start of the cycle
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
```