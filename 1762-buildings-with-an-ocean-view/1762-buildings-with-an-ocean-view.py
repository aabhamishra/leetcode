from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # for building b, sea(b) if height(b) > height(x) for all x to right of b
        # sorted in increasing order is important
        # stack - left to right.
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
            
            stack.append(i)
        
        return stack