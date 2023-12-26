# Logistics
Attempt date: 25 December 2023
Runtime: 2 ms
Memory Usage: 52.8 MB

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The intuition behind this algorithm is to compute the product of all elements to the left and right of each element in the array efficiently. The two-pass approach allows us to avoid using division and achieve a time complexity of O(n).

# Approach
<!-- Describe your approach to solving the problem. -->
1. Initialize product array: Create an array product to store the final result. This array will be the product of all elements to the left and right of each element in the original array.

2. Establish post-product from right to left:

Start from the second-to-last element (index n - 2) and go towards the first element (index 0).
For each element at index i, set product[i] to be the product of the element to its right and the corresponding product value from the previous step (product[i + 1]).
Multiply with pre-product from left to right:

3. Initialize a variable left to keep track of the product of elements to the left of the current element.
Start from the second element (index 1) and go towards the last element (index n - 1).
For each element at index i, multiply the current product[i] with left (the product of elements to its left) and update left by multiplying it with the element to its left (nums[i - 1]).
4. Return the product array: The product array now contains the product of all elements except itself for each element in the original array.

This algorithm utilizes two passes through the input array to compute the left and right products efficiently without using division.

# Complexity
- Time complexity: O(n)
This is because we have two passes over the input array, each having a time complexity of O(n).
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
- Space complexity: O(1)
We use O(1) auxiliary space aside from the output array.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->


# Code
```
class Solution {
    public int[] productExceptSelf(int[] nums) {

        int n = nums.length;
        int[] product = new int[n];
        
        product[n - 1] = 1;

        // establish post-product
        for (int i = n - 2; i >= 0; i--) {
            product[i] = nums[i + 1] * product[i + 1];
        }
        
        int left = 1;
        // multiply with pre-product
        for (int i = 1; i < n ; i++) {
            left = nums[i - 1] * left;
            product[i] *= left;
        }

        return product;

    }
}
```​