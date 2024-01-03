## Intuition
- The algorithm iterates through each row in the bank, counting the number of `1` characters in each row.
- If the count (`curr`) is not zero, it implies the presence of lasers.
- The algorithm accumulates the total number of beams by multiplying the current count (`curr`) with the count from the previous row (`prev`).
- This approach efficiently counts the number of beams formed by consecutive '1' characters in the bank.

## Approach
1. Get the dimensions of the bank: `m` (number of rows) and `n` (number of columns).
2. If there is only one row in the bank (`m == 1`), return 0, as a single row cannot form a beam.
3. Initialize variables `beams` and `prev` to 0.
4. Iterate through each row in the bank:
   - Initialize a variable `curr` to 0.
   - Count the number of '1' characters in the current row (`row`) and store the count in `curr`.
   - If `curr` is not zero:
     - Increment `beams` by the product of `prev` and `curr`.
     - Update `prev` to `curr`.
5. Return the total number of beams (`beams`).

## Complexity
- Time complexity: $O(1)$
The algorithm iterates through each row and column in the bank once. The time complexity is O(m * n), where `m` is the number of rows and `n` is the number of columns in the bank.

- Space complexity: $O(m*n)$
The algorithm uses a constant amount of extra space for variables (`m`, `n`, `beams`, `prev`, `curr`, `row`, `j`). The space complexity is O(1).

## Code
```
class Solution {
    public int numberOfBeams(String[] bank) {

        int m = bank.length;
        if(m == 1) return 0;

        int n = bank[0].length();

        int beams = 0, prev = 0;

        for(String row : bank ){
            int curr = 0;

            for(int j = 0; j < n; j++) {
                if(row.charAt(j) == '1') curr++;
            }

            if(curr != 0) {
                beams += prev*curr;
                prev = curr;
            }
        }
        return beams;
    }
}
```