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
    public void reorderList(ListNode head) {
       ListNode slow = head;
       ListNode fast = head.next;

       while(fast != null && fast.next != null) {
           slow = slow.next;
           fast = fast.next.next;
        } 

        ListNode second = slow.next;
        slow.next = null;

        ListNode prev = null;

        while(second != null) {
            ListNode temp = second.next;
            second.next = prev;
            prev = second;
            second = temp;
        }

        ListNode tmp1 = null, tmp2 = null;
        ListNode first = head;
        second = prev;

        while(second != null) {
            tmp1 = first.next;
            tmp2 = second.next;

            first.next = second;
            second.next = tmp1;
            first = tmp1;
            second = tmp2;
        }
    }
}