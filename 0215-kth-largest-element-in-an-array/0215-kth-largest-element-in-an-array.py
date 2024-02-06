class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for i in nums[k:]:
            if i > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, i)
        
        return minHeap[0]
