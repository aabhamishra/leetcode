

## Intuition
The algorithm aims to find the total amount of rainwater that can be trapped between the bars represented by the array `height`. It uses the two-pointer approach to determine the trapping height and iterates until the pointers meet.

### How To Move The Pointers

**Incrementing Start Pointer**

When the height of the bar at the current start position (`start_height`) is less than or equal to the height of the bar at the end position (`end_height`), it indicates that the limiting factor for trapping rainwater is the `start_height`. Therefore, we increment `start` to find the next potentially higher bar. While doing this, we calculate the trapped rainwater at each step based on the difference between `start_height` and the height of the bar at the current start position (`height[start]`).

**Decrementing End Pointer**

On the other hand, when the height of the bar at the end position (`end_height`) is less than `start_height`, it indicates that the limiting factor for trapping rainwater is the `end_height`. Therefore, we decrement end to find the next potentially higher bar from the right. While doing this, we calculate the trapped rainwater at each step based on the difference between `end_height` and the height of the bar at the current end position (`height[end]`).




## Approach
1. Initialize pointers `start` and `end` at the beginning and end of the array `height`.
2. Initialize `water` to 0, representing the total trapped rainwater.
3. While `start` is less than `end`:
    - Retrieve the heights of the bars at positions `start` and `end` (`start_height` and `end_height`).
    - If `start_height` is less than or equal to `end_height`:
        - Increment `start` while the height at `start` is less than or equal to `start_height`.
        - Incrementally add the trapped rainwater based on the difference between `start_height` and the height at `start`.
    - If `end_height` is less than `start_height`:
        - Decrement `end` while the height at `end` is less than or equal to `end_height`.
        - Incrementally add the trapped rainwater based on the difference between `end_height` and the height at `end`.
4. Return the total trapped rainwater.

### Time Complexity $O(n)$
The algorithm iterates through the array using the two-pointer approach. In each iteration, it performs constant-time operations. Therefore, the time complexity is O(N), where N is the length of the array.

### Space Complexity $O(1)$
The algorithm uses a constant amount of extra space, resulting in a space complexity of O(1).

## Code
**Python**
```
class Solution:
    def trap(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        water = 0

        while start < end:
            start_height, end_height = height[start], height[end]

            # limiting factor is start_height
            if start_height <= end_height:
                start += 1
                # Increase start while height at start is lesser than start_height
                # This means that rainwater will be trapped with respect to start_height
                while start < end and height[start] <= start_height:
                    water += start_height - height[start]
                    start += 1
            else:
                end -= 1
                # Decrease end while height at end is lesser than end_height
                # This means that rainwater will be trapped with respect to end_height
                while start < end and height[end] <= end_height:
                    water += end_height - height[end]
                    end -= 1
        
        return water
```

**Java**
```
class Solution {
    public int trap(int[] height) {
        int start = 0;
        int end = height.length - 1;
        int water = 0;

        while(start < end) {
            int s = height[start];
            int e = height[end];

            if(s <= e){
                
                start++;
                
                while(start < end && height[start] <= s){
                    water = water + s - height[start];
                    start++;
                } 
            }
            else{
                
                end--;

                while(start < end && height[end] <= e){
                    water = water + e - height[end];
                    end--;
                } 
            }
        }

        return water;
    }
}
```