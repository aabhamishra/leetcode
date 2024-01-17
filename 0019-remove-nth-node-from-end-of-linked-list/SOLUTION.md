## Intuition
We want to remove the nth node from the end. However, as the list is singly linked, we should first retrieve the value of `remove` - the index of that node from the start. For this, we iterate to the end of the list to get the total length of the list `len`. We notice that:

`remove = len - n` (0-indexed)

Now, there are two cases to handle:

1. `remove is 0`: This means that we need to remove the first element from the list. We return `head.next`. This can happen either when there is only one node in the liked list (in which case the return value will be `None`) or when there are many nodes but n equals len.

2. `remove is not 0`: This means we have to remove an element in the midle or end. For this we iterate a dumy pointer till it reaches the node **previous** to the one that will be removed. Once we have that node `prev`, we update `prev.next` to point to  one node over: `prev.next.next`. We finally return the original head. 

## Approach

1. **Calculate Length**: Traverse the linked list to calculate its length.
2. **Remove Node**: Traverse the list again to find the node just before the one to be removed and update its `next` pointer to skip the node to be removed.

The algorithm returns the modified head of the linked list.

## Complexity
- Time complexity: $O(n)$
The time complexity is O(N), where N is the number of nodes in the linked list. The algorithm traverses the list twice, once to calculate the length and once to find the node to be removed.

- Space complexity: $O(1)$
The space complexity is O(1) as the algorithm uses only a constant amount of extra space for variables (`len`, `dummy`, and `i`).

## Code
```python
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
        
        # get 0-indexed node to remove from start
        remove = len-n
    
        # case where first node should be removed
        if remove == 0:
            return head.next
        
        # all other cases - remove node in middle or end
        dummy = head
        i = 0

        # loop to get the node before the one to remove
        while i < remove - 1:
            dummy = dummy.next
            i+=1
        
        dummy.next = dummy.next.next
 
        return head      
```