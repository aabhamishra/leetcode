# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # define the pointers
        slow, fast = head, head.next

        # iterate so that slow pointer reaches the middle of list 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # start of second half of list
        second = slow.next
        # first half ends, so point it to None
        slow.next = None

        # reverse second half of list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # combine lists now in alternate indices
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        

        