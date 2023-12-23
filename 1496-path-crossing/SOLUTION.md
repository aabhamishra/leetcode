# Logistics
Attempt date: 22 December 2023
Runtime: 1 ms
Memory Usage: 41.94 MB

# Intuition
For paths to cross, the current location of the pointer has to have already been visited. This means that we need y to track every location that has been visited. As the locations are on a 2D plane and contain 2 variables, we need a way to store two variables in each entry. 

The intuitive solution to this is a `Pair<Integer, Integer>` which stores the x and y coordinates of each location. 

Now, as our algorithm has to sotre all the distinct visited locations, it is best to use a `HashSet<Pair<Integer, Integer>>`. 

Finally, we also use a HashSet to store moves associated with each direction. This step can be avoided to decrease memory space, but this algorithm uses it for cleaner code.

<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
1. Define and initialize a`HashSet<Character, Pair<Integer, Integer>> moves` to track moves associated with each of the four directions.
2. Define an empty `HashSet<Pair<Integer, Integer>> visited` to track already visited coordinates. 
3. Initialize two integers, curr_x=0 and curr_y=0 to track current coordinates. Add `new Pair(0, 0)` to `visited` as this is the origin.
4. Iterate over each direction in the String `Path`.
    a. From `moves`, retrieve the value i.e. move associated with the direction.
    b. Add the x and y coordinates of move to curr_x and curr_y. This is the new position after the move.
    c. Check if this pair (curr_x, curr_y) is already present in visited. If so, return true as paths are crossing. Else, add the pair to visited.
5. Return false at end as this denotes that the paths did not cross and we have reached the end of the string `path`.
# Complexity
- Time complexity: O(n)
The dominant execution is the for loop where we iterate over every character in `path` till we find a recurrence, if any. Each iteration takes constant time as we are using HashSets to store the information. Hence, the time complexity is O(n) where n is the number of directions in the string `path`.

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(n)
`moves` takes constant space. `visited` takes up space proportional to the number of directions in the input string. Hence space complxity will be O(n).
<!-- Add your space complexity here, e.g. $$O(n)$$ -c ->

# Code
```
class Solution {
    public boolean isPathCrossing(String path) {
        HashMap<Character, Pair<Integer, Integer>> moves = new HashMap();
        moves.put('N', new Pair(0, 1));
        moves.put('S', new Pair(0, -1));
        moves.put('W', new Pair(-1, 0));
        moves.put('E', new Pair(1, 0));
          
        HashSet<Pair<Integer, Integer>> visited = new HashSet<>();
        visited.add(new Pair(0, 0));

        int x = 0;
        int y = 0;

        for(Character move : path.toCharArray()) {
            x += moves.get(move).getKey();
            y += moves.get(move).getValue();

            if(visited.contains(new Pair(x,y))) return true;
            visited.add(new Pair(x, y));
        }

        return false;
    }
}
```