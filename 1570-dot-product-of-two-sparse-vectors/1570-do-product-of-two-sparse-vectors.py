from typing import List

class SparseVector:

    def __init__(self, nums: List[int]):
        
        self.non_zero = []
        
        for i in range(len(nums)):
            if nums[i] != 0:
                self.non_zero.append((i, nums[i]))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p1, p2 = 0, 0
        res = 0

        while p1 < len(self.non_zero) and p2 < len(vec.non_zero):
            if self.non_zero[p1][0] > vec.non_zero[p2][0]:
                p2+=1
            elif self.non_zero[p1][0] < vec.non_zero[p2][0]:
                p1+=1
            else:
                res += self.non_zero[p1][1] * vec.non_zero[p2][1]
                p1+=1
                p2+=1
                     
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)