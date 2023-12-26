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