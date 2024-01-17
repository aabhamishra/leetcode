# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        dummy = head
        # get the length
        while dummy:
            len+=1
            dummy = dummy.next

        # get 0-indexed element to remove from start
        remove = len-n
    
        # case where first element should be removed
        if remove == 0:
            return head.next
        
        # all other cases - remove element in middle or end
        dummy = head
        i = 0

        # loop to get the element before the one to remove
        while i < remove - 1:
            dummy = dummy.next
            i+=1
        
        dummy.next = dummy.next.next
 
        return head