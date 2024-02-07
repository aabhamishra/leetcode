## Intuition
The problem involves finding the sum of all nodes' values in a binary search tree (BST) within the range `[low, high]`. The algorithm efficiently computes the sum of node values within the specified range in the BST by leveraging a recursive approach. By traversing the BST and selectively accumulating node values based on the range criteria, it achieves the desired result without examining every node in the tree.


## Approach
The algorithm recursively traverses the BST and accumulates the sum of node values that fall within the specified range `[low, high]`.

1. **Base Case**: If the current node is null (i.e., a leaf node or an empty subtree), return 0.

2. **Range Sum Calculation**: At each node, if the node's value falls within the range `[low, high]`, add its value to the `sum`. Then, recursively call the function on both its left and right children.

3. **Pruning**: If the node's value is greater than `high`, traverse only its left subtree since all values in the right subtree will be greater than `high`. Similarly, if the node's value is less than `low`, traverse only its right subtree since all values in the left subtree will be less than `low`.

4. **Sum Accumulation**: Return the accumulated sum after traversing the entire BST.

The algorithm returns the sum of node values within the specified range `[low, high]` in the BST.

## Complexity
- Time complexity: $O(N)$
The time complexity is O(N), where N is the number of nodes in the BST. In the worst case, the algorithm traverses all nodes of the BST once.

- Space complexity: $O(H)$
The space complexity is O(H), where H is the height of the BST. The recursion stack space is proportional to the height of the BST due to the recursive nature of the algorithm.

# Code
```java
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
```