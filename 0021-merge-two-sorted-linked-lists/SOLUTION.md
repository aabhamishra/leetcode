## Intuition

The algorithm uses a straightforward iterative approach to merge the two sorted linked lists. The algorithm compares the values of the nodes at the current positions in `list1` and `list2`, and appends the smaller value to the merged list. The pointers are then updated accordingly. The process continues until one of the input lists becomes empty, and any remaining nodes from the non-empty list are appended to the merged list.

The algorithm intuitively merges two sorted linked lists by comparing the values of their nodes at each step. The use of a `dummy` node simplifies retrieving the head of the list, and the pointers (`head`, `list1`, and `list2`) are efficiently updated to create the merged list in sorted order.

## Approach

1. Initialize a `dummy` node and a `head` pointer to the next node after `dummy`.
2. Iterate through both lists (`list1` and `list2`) using a `while` loop until one of them becomes `null`.
3. Compare the values of the current nodes in `list1` and `list2`.
4. Append the node with the smaller value to the merged list, and update the pointers accordingly.
5. Continue the iteration until one of the input lists becomes empty.
6. If there are remaining nodes in `list1` or `list2`, append them to the merged list.
7. Return the merged list starting from the next node after the `dummy` node.

## Complexity
- Time complexity: $O(m+n)$
The time complexity is O(m + n), where m and n are the lengths of `list1` and `list2`, respectively. The algorithm iterates through both lists once.

- Space complexity: $O(1)$
The space complexity is O(1) as the algorithm only uses a constant amount of extra space for pointers (`dummy` and `head`).

## Code
```java
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(101, new ListNode());
        ListNode head = dummy.next;

        while(list1 != null && list2 != null) {    
            if (list1.val < list2.val) {
                head.next = new ListNode(list1.val);
                head = head.next;
                list1 = list1.next;
            } else {
                head.next = new ListNode(list2.val);
                head = head.next;
                list2 = list2.next;
            }
        }

        if(list1 != null) head.next = list1;

        if(list2 != null) head.next = list2;

        return dummy.next.next;
    }
}
```