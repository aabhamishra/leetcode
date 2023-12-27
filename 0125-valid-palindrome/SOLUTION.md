# Logistics
Attempt date: 27 December 2023
|| Runtime: 2 ms (beat 99% of other submissions)
|| Memory Usage: 46.9 MB

# Intuition
The fist solution I came up with constructs a new string from the alphanumeric characters in the string, and then checks if this new string is a palindrome. This is a perfectly okay approact, but there is another approach that takes O(1) auxiliary space and iterates over the input string just once.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
In this approach, we identify two pointers: start and end. `start` is initialized to 0, and `end` is initialized to `string.length() - 1`. These pointers will point to the first and last elements of the input string.

We then iterate over the string while `start < end`. If the character at start is not alphanumeric, we increment start by 1. Similarly, if the character at end is not alphanumeric, we increment end by 1. This is so that we can skip over the non-alphanumeric characters in the string while comparing without having to create a new string with just the alphanumeric characters.

If neither of the two above conditions is satisfied, we have encountered an alphanumeric pair that needs to be checked for equality. Convert the characters to lower case and check if they are equal. If not, return `false` as the string is not palindromic. 

Finally, return true outside of the loop, as we have reached the end of execution and can conclude that the input string is palindromic.

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: O(n)
We pass over the string just once. The execution of statements takes O(1) time for each iteration.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
We only declare two integers as additional memory for execution (start and end).
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution {
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() -1;

        while(start < end) {
            if(!Character.isLetterOrDigit(s.charAt(start))) start++;
            else if(!Character.isLetterOrDigit(s.charAt(end))) end--;
            else {
                if(Character.toLowerCase(s.charAt(start)) != Character.toLowerCase(s.charAt(end))) return false;
                start++;
                end--;
            }
        }
        return true;
    }
}
```