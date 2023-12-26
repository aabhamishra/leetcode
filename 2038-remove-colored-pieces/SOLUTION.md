# Winner of the Game Explanation

## Intuition
The algorithm aims to determine the winner of a game played by Alice and Bob, where they take alternating turns removing pieces from a line. What to note here is that Alice starts playing first. Hence, alice should have more playable turns (or group of 3 consecutive A's) than Bob. 

## Approach
1. **Initialization:**
   - Initialize variables `A` and `B` to represent the scores of Alice and Bob, respectively.
   - Variable `curr` keeps track of consecutive occurrences of a color, and `isA` is a boolean flag indicating whether the current color being processed belongs to player A.

2. **Iterate Through the String:**
   - Use a for loop to iterate through each character in the `colors` string.

3. **Update Scores:**
   - If the current character is 'A':
      - If the previous color was also 'A', increment `curr` to count consecutive occurrences.
      - If the previous color was 'B', update player B's score (`B`) based on the number of consecutive occurrences (`curr`) beyond the initial three, then reset `curr` to 1 for player A.
   - If the current character is 'B':
      - If the previous color was 'B', increment `curr` to count consecutive occurrences.
      - If the previous color was 'A', update player A's score (`A`) based on the number of consecutive occurrences (`curr`) beyond the initial three, then reset `curr` to 1 for player B.

4. **Update Scores for the Last Sequence:**
   - After the loop, check if there is a last sequence that needs to be accounted for. If `curr` is greater than or equal to 3, update the respective player's score accordingly.

5. **Determine Winner:**
   - Finally, compare the scores of players A and B. If `A` is greater than `B`, return `true` (indicating Alice wins); otherwise, return `false` (indicating Bob wins).

## Time Complexity
The time complexity of this algorithm is O(n), where n is the length of the input string `colors`. The algorithm iterates through the string once.

## Space Complexity
The space complexity is O(1) as the algorithm uses a constant amount of space, regardless of the input size. It only requires a few variables to keep track of scores and consecutive occurrences.


# Code
```
class Solution {
    public boolean winnerOfGame(String colors) {
        int A = 0;
        int B = 0;

        int curr = 0;
        boolean isA = false;
        for( int i = 0; i < colors.length(); i++) {
            char c = colors.charAt(i);

            if(c == 'A') {
                if(isA == true) curr++;
                else {
                    if(curr >= 3) B = B + curr - 2; 
                    curr = 1;
                    isA = true;
                }
            } else {
                if(isA == true) {
                    if(curr >= 3) A = A + curr - 2;
                    curr = 1;
                    isA = false;
                }
                else curr++;
            }    
        }

        if(curr >= 3) {
            if(isA) A+= curr - 2;
            else B +=curr - 2;
        } 

        if(A > B) return true;
        
        return false;
    }
}
```