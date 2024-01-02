## Objective
The algorithm aims to group numbers from an input array `nums` into rows of a matrix based on their frequency. It utilizes a HashMap (`freq`) to track the frequency of each number and constructs the matrix incrementally.

## Approach
1. Initialize an empty list `res` to represent the matrix, with the first row already added.
2. Use a HashMap `freq` to keep track of the frequency of each number encountered in the array.
3. Iterate through each number `num` in the array:
   - Obtain the current frequency of `num` from the `freq` map.
   - Increment the frequency in the `freq` map.
   - Check if the current row index `size` is greater than or equal to the frequency:
     - If true, add `num` to the corresponding row in the matrix (`res`).
     - If false, create a new row with `num` and increment the `size`.
4. Return the resulting matrix.

## Intuition Explanation
- The algorithm progressively builds rows of the matrix based on the frequency of each number.
- It maintains a `size` variable to keep track of the current row index in the matrix.
- By checking the frequency against the row index, the algorithm ensures that each number is placed in the row corresponding to its frequency.
- This approach allows for efficient grouping of numbers with the same frequency and results in a matrix representation of the input array.

## Example
Consider the array `[1, 2, 1, 3, 2, 4]`:
- For `num = 1`, the matrix is `[[1]]`.
- For `num = 2`, the matrix becomes `[[1], [2]]`.
- For `num = 1` (second occurrence), the matrix becomes `[[1, 1], [2]]`.
- For `num = 3`, the matrix becomes `[[1, 1], [2, 3]]`.
- For `num = 2` (second occurrence), the matrix becomes `[[1, 1], [2, 3, 2]]`.
- For `num = 4`, the matrix becomes `[[1, 1], [2, 3, 2, 4]]`.

### Time Complexity: $O(n)$
The algorithm iterates through each number in the array, performing constant-time operations. The time complexity is O(N), where N is the length of the input array.

### Space Complexity: $O(n)$
The algorithm uses additional space for the matrix (`res`), the frequency map (`freq`), and other variables. The space complexity is O(N), where N is the length of the input array.

```
class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<List<Integer>> res = new ArrayList();
        res.add(new ArrayList<Integer>());
        int size = 0;

        Map<Integer, Integer> freq = new HashMap();

        for(int num : nums) {
            int frequency = freq.getOrDefault(num, 0);
            freq.put(num, frequency + 1);

            if(size >= frequency) {
                res.get(frequency).add(num);
            } else {
                List<Integer> l = new ArrayList<>();
                size++;
                l.add(num);
                res.add(l);
            }
        }

        return res;
    }
}
```
