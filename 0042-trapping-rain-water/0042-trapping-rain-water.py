class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
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