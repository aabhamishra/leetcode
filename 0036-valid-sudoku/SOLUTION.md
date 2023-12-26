# Logistics
Attempt date: 26 December 2023
Runtime: 13 ms
Memory Usage: 45.3 MB

# Intuition
The algorithm is based on the observation that in a valid Sudoku board, no number should be repeated in the same row, column, or 3x3 subgrid (box). The algorithm uses a HashSet (seen) to keep track of the numbers encountered so far in each row, column, and box. If it encounters a number that is already present in the HashSet for any of these categories, it immediately returns false as the board is invalid; otherwise, it returns true at the end.

# Approach

1. Initialize HashSet:
Create a HashSet called seen to keep track of unique numbers encountered in rows, columns, and boxes.
Iterate Through the Board:

2. Use nested loops to iterate through each cell in the 9x9 Sudoku board.
Check Each Number:

    1. For each cell, retrieve the number present in that cell.
    2. If the number is not '.', indicating an empty cell:
        - Check if adding the number with "row" + row index is present in the HashSet (seen). If it is, return false as it violates the Sudoku rule for rows.
        - Check if adding the number with "col" + column index is present in the HashSet (seen). If it is, return false as it violates the Sudoku rule for columns.
        - Check if adding the number with "box" + (row index / 3) + (column index / 3) is present in the HashSet (seen). If it is, return false as it violates the Sudoku rule for the 3x3 boxes.

3. Return Result:
If the algorithm successfully iterates through the entire board without encountering any violations, return true, indicating that the Sudoku board is valid.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: O(n) as we are iterating over each element just once. Checking for duplicate entries in hashset also has O(1) time complexity. Hence. the total time complexity is O(n).
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(n)
We are using O(n) space to store the non-empty elements from the board in the HashSet. 
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution {
   public boolean isValidSudoku(char[][] board) {
    Set seen = new HashSet();
    for (int i=0; i<9; i++) {
        for (int j=0; j<9; j++) {
            char number = board[i][j];
            if (number != '.')
                if (!seen.add(number + "row" + i) ||
                    !seen.add(number + "col" + j) ||
                    !seen.add(number + "box" + i/3 + j/3))
                    return false;
        }
    }
    return true;
}
}
```

