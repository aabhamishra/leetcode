/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum = 0;
    public int rangeSumBST(TreeNode root, int low, int high) {
        // if node is between value, add to sum and check both children
        // if node > high, check only left subtree
        // if node < low, check only right subtree

        if(root == null) return 0;

        if(low <= root.val && root.val <= high) {
            sum += root.val;

            rangeSumBST(root.left, low, high);
            rangeSumBST(root.right, low, high);
        } else if(root.val > high) {
            rangeSumBST(root.left, low, high);
        } else {
            rangeSumBST(root.right, low, high);
        }

        return sum;
    }
}