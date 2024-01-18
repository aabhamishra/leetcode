There are two possible solutions for this problem. Using a HashSet is pretty intuitive but leads to O(n) extra space. To optimize space, we utilize the second solution, which involves using two pointers working at different speeds in what is known as Floyd's Tortoise and Hare algorithm.

## First Solution - HashSet

The first solution uses a HashSet to keep track of unique nodes while traversing the linked list. If a node is encountered that already exists in the HashSet, it means there is a cycle in the linked list. Otherwise, the node is added to the HashSet, and the traversal continues until the end of the list.

#### Intuition

- Traverse the linked list.
- Use a HashSet to store unique nodes.
- If a node is already present in the HashSet, there is a cycle, and the function returns `true`.
- If the traversal reaches the end of the list without encountering a duplicate node, there is no cycle, and the function returns `false`.

#### Time Complexity $O(n)$
The time complexity is O(N), where N is the number of nodes in the linked list. This is because, in the worst case, the algorithm needs to traverse the entire list.

#### Space Complexity $O(n)$
The space complexity is O(N) due to the HashSet, where N is the number of nodes in the linked list.

#### Code
```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> unique = new HashSet();

        while(head != null) {
            if(!unique.add(head)) return true;
            head = head.next;
        }

        return false;
    }
}
```
## Second Solution - Two Pointers

The second solution, also known as Floyd's Tortoise and Hare algorithm, uses two pointers, one slow and one fast, to detect cycles in a linked list. If there is a cycle, the fast pointer will eventually catch up to the slow pointer.

#### Intuition

- Initialize two pointers, slow and fast, both pointing to the head of the linked list.
- Move the slow pointer one step at a time and the fast pointer two steps at a time.
- If there is a cycle, the fast pointer will eventually catch up to the slow pointer.
- If there is no cycle, the fast pointer will reach the end of the list.

#### Time Complexity $O(n)$

- The time complexity is O(N), where N is the number of nodes in the linked list. This is because, in the worst case, both pointers will traverse the entire list.

#### Space Complexity $O(1)$

- The space complexity is O(1) as the algorithm uses only a constant amount of extra space for the two pointers.

## Code
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
```