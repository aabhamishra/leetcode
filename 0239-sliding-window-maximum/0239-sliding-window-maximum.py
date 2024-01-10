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