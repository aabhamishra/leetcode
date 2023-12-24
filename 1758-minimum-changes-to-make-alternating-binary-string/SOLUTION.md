# Logistics
Attempt date: 24 December 2023
Runtime: 2 ms
Memory Usage: 43 MB

# Intuition
The question asks us to count minimum operations to create an alternating String. Now, there are only two variations of a binary alternating string:

1. "1010101010101..." - String starts with '1'
    At odd indices, character is '0'.
    At even indices, character is '1'.
2. "0101010101010..." - String starts with '0'
    At odd indices, character is '1'.
    At even indices, character is '0'.

This is all the information we need. To solve the problem, we keep two counters, each measuring the number of corrections to reach a variation of the alterating string.

We iterate over the string and increment the counters if we spot the wrong character for the association binary variation. At the end, we return the minimum of the two counters.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->
1. Initialize two counters: `start1 = 0` and `start0 = 0`.
2. Iterate over the string:
-> If the current index is odd:
If character at the index is `0`, this means its correct for start1 but incorrect for start0. Hence, increment start0 by 1 as we have found a correction to be made. 
Else, this means the character is `1`, meaning that a correction is needed for start1 instead. Hence, increment start1.
-> If the current index is even:
With the same logic as above, if the character at index is `1`, increment start1. Else, increment start0.


3. FInally return the minimum of start0 and start1. This is the minimum number of corrections needed. 

# Complexity
- Time complexity: O(n)
This is as we are only iterating over the array once, updating both cointers as we move along.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->


- Space complexity: O(1)
We are only initializeing two int counters and accessing the string as is.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution {
    public int minOperations(String s) {
        int start0 = 0;
        int start1 = 0;

        char[] arr = s.toCharArray();
        for(int i = 0; i < arr.length; i++) {
            if(i % 2 == 0) {
                if(arr[i] == '0') start1++;
                else start0++;
            } else {
                if(arr[i] == '0') start0++;
                else start1++;
            } 

        }

        return Math.min(start0, start1);
    }
}
```