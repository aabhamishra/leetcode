# Intuition and Approach
The problem talks about dividing the String into two parts, the left and right substrings. 

value(left) = number of zeros in left substring
value(right) = number of zeros in the right substring

In this approach, lets keep track of three variables: 
1. `curr_max`  
2. `global_max`
3. `split_index`

All are intialized to 0, representing the base case.

The approach is that when we first iterate over the chracters in the string, there are only two possibilities: a 0 or a 1. 

When the character in question is a `0`, adding it to the left substrng would increase value(left), so in this case, we `curr_max++`. Conversely, if the character is a `1`, adding it to left would decrease value(right), so we `curr_max-- `. 

Now with every iteration, if curr_max is greater than global_max, we update global_max. In that case, we also update split index as the current index. 

As we cannot have empty substrings, we only iterate ^^ for elements from indices 0 to n-2 (n =length of string). 

Finally, once we determine the split index with the maximum global_max, we then iterate once more over the string to find the return value. From index 0 to split_index, we add 1 to the value for every `0`. From index split_index + 1 to the end of the string, we add 1 to the return value for every `1`. 

Finally, we return the value.
<!-- Descrby ibe your first thoughts on how to solve this problem. -->

# Complexity
- Time complexity: O(n)
We iterate over the array twice, which means the complexity is O(2n), which is equivalent to O(n).
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
The space complexity for this algorithm is O(1) as we are only storing three variables in memory and the atring is being accessed in place. 
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution {
    public int maxScore(String s) {
        int max = 0;
        int curr_max = 0;
        int index = 0;

        for(int i = 0; i < s.length() - 1; i++) {
            if(s.charAt(i) == '0') max++;
            else max--; 

            if(max >= curr_max) {
                curr_max = max;
                index = i;
            }
        }

        max = 0;

        for(int i = 0; i <= index; i++){
            if(s.charAt(i) == '0') max++;
        }
        for(int i = index + 1; i < s.length(); i++) {
            if(s.charAt(i) == '1') max++;
        }

        return max;
    }
}
```