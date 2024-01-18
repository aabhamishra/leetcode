## Intuition

The algorithm efficiently creates a deep copy of a linked list with random pointers by interweaving new nodes, assigning random pointers, and then extracting the new list. This approach ensures that the random pointers are correctly mapped to the corresponding nodes in the new list.

## Approach

The algorithm follows a three-step approach:

1. **Interweave New Nodes**: Traverse the original linked list and, for each node, insert a new node with the same value right after it. This interweaves the new nodes with values and the `next` pointers.
2. **Assign Random Pointers**: Iterate through the interweaved list and assign the `random` pointers for the new nodes based on the corresponding `random` pointers of the original nodes.
3. **Extract New List**: Repoint the new nodes' next pointers to weave out the old nodes. Return the head of the new list.

## Complexity
- Time complexity:
The time complexity is O(N), where N is the number of nodes in the original linked list. The algorithm traverses the list three times in a single pass.

- Space complexity:
The space complexity is O(1) as the algorithm uses only a constant amount of extra space for pointers (`curr`, `next`, `old`).

## Code
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head

        # interweaves new nodes with values and next
        while curr:
            next = curr.next
            curr.next = Node(curr.val, next)
            curr = curr.next.next

        curr = head
        # add random pointer
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        # weave out old nodes
        curr = head.next

        while curr:
            old = curr.next
            curr.next = old.next if old else None
            curr = curr.next
        
        return head.next
```