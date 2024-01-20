class Solution:
    def findDuplicate(self, nums: [int]) -> int:
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