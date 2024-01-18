
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
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
        

