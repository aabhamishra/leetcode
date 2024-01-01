## Logistics
Attempt Date: January 1 2024
|| Runtime: 36 ms
|| Memory: 53 MB

## Intuition
Three sum is an extended version of the two sum II problem. To solve this question, we will use a two pointer approach. The intuition for this question is that to create a sum of three numbers that equals 0, at least one of the numbers has to be negative, or all three have to equal 0. 

let's have the indices be `i, j, k`. `i` represents the first number, which will always be negative or 0. for each probable `i`, we use the two sum algorithm to find combinations of `j` and `k` so that:

`nums[i] + nums[j] + nums[k] = 0`


## Approach
1. We first initialize the return List of Lists `res` and sort the input array `nums`.
2. If `nums[i]` is greater than 0, that means that the smallest possible integer in this array is now positive. As mentioned above, we cannot create a sum euqal to 0 from these three numbers. Hence, we break from the loop.
3. We iterate `i` through `nums` from index `0` to `nums.length - 2`.
    - We first skip duplicate elements of i when i != 0. The use of the condition `i != 0` is to make sure the first iteration of the loop is always executed.
    - Then, we initialize `j = i+1` and `k = nums.length - 1`.
    - Now, we go through every possibility of j and k such that the sum is 0. If a combination equals 0, we add it to `res`. Then, we increase j and decrease k, skipping duplicate values. 
    - If sum does ot equal 0, there are two possibilites: `sum < 0` or `sum > 0`.
        - If `sum < 0`, this means that `nums[j]` is too small, and we need to check for the next smallest number. Hence, we execute `j++`. 
        - If `sum < 0`, this means that `nums[k]` is too big, and we need to check for the next biggest number. Hence, we execute `k--`. 

4. Outside of the loop, return `res`.

## Complexity
- Time complexity: O(n^2)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->


- Space complexity: O(n)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for(int i = 0; i < nums.length - 2; i++) {

            // if the smallest element is greater than 0, we cannot add three elements to get 0.
            if (nums[i] > 0) break;

            // skip duplicates for i
            if(i > 0 && nums[i] == nums[i-1]) continue;

            int j = i+1;
            int k = nums.length - 1;

            while(j < k) {
                int sum = nums[i] + nums[j] + nums[k];

                if(sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));

                    while(j < k && nums[j] == nums[j+1]) j++;
                    while(j < k && nums[k] == nums[k-1]) k--;

                    j++;
                    k--;
                } else if (sum < 0){
                    j++;
                } else {
                    k--;
                }
            }
        }

        return res;
    }
}
```