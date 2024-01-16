## Intuition

The algorithm uses a classic iterative approach to reverse the linked list. It maintains three pointers: `curr`, `prev`, and `next`. The `curr` pointer iterates through the list, and at each step, the algorithm reverses the direction of the `next` pointer of the current node to point to the previous node. The `prev` pointer is then updated to `curr`, and `curr` moves to the next node.

## Approach

1. Initialize two pointers, `curr` and `prev`, to the head of the linked list.
2. Iterate through the list using a `while` loop until `curr` becomes `null`.
3. Inside the loop, store the next node of `curr` in a temporary variable `next`.
4. Reverse the direction of the `next` pointer of `curr` to point to `prev`.
5. Update `prev` to `curr` and move `curr` to the next node (`next`).
6. Continue the iteration until `curr` becomes `null`.
7. Return the reversed linked list, represented by the new head (`prev`).

## Complexity
- Time complexity: $O(n)$

The time complexity is O(N), where N is the number of nodes in the linked list. The algorithm iterates through each node once.

- Space complexity: $O(1)$
The space complexity is O(1) as the algorithm only uses a constant amount of extra space for pointers (`curr`, `prev`, `next`).

## Code
```
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        
        ListNode curr = head;
        ListNode prev = null;

        while(curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
}
```