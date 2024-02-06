## Intuition

The algorithm efficiently finds the kth largest element in the array by using a min-heap. By maintaining a min-heap with the k largest elements seen so far, the algorithm ensures that the kth largest element is always at the top of the heap. As a result, it avoids sorting the entire array and only focuses on the k largest elements, leading to improved time complexity.

## Approach

1. **Min-Heap Initialization**: Initialize a min-heap (`PriorityQueue`) with the first k elements of the array.

2. **Iterative Update**: Iterate through the remaining elements of the array.
    - If the current element is greater than the smallest element in the min-heap (i.e., `minHeap.peek()`), remove the smallest element from the min-heap and add the current element to it.

3. **Result Extraction**: After processing all elements, the kth largest element will be at the top of the min-heap. Return this element as the result.
## Complexity
- Time complexity: $O(N*logk)$
The time complexity is O(N log k), where N is the length of the input array `nums` and k is the value of the parameter `k`. The algorithm iterates through each element of the array and performs heap operations, each of which takes O(log k) time.

- Space complexity: $O(k)$
The space complexity is O(k) as the min-heap stores at most k elements.

## Code
**Python**
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for i in nums[k:]:
            if i > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, i)
        
        return minHeap[0]

```

**Java**
```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        // min heap ftw
        PriorityQueue<Integer> minHeap = new PriorityQueue();

        for(int i = 0; i < k; i++) {
            minHeap.offer(nums[i]);
        }

        for(int i = k; i < nums.length; i++) {
            if(nums[i] > minHeap.peek()) {
                minHeap.poll();
                minHeap.offer(nums[i]);
            }
        }

        return minHeap.peek();
    }
}
```