# Logistics
Attempt date: 20 December 2023
|| Runtime: 4 ms
|| Memory: 41.5 MB

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Hashtables and arrays can both be used to track frequencies of letters in the strings. Arrays are useful when you need to store a fixed number of elements of the same type, access them by index, and iterate over them in order. Hash tables are ideal when you need to store variable number of elements of different types, access them by key, and perform frequent insertions and deletions. 

Clearly, arrays are better posed for this situation.

# Approach
<!-- Describe your approach to solving the problem. -->
1. If lenghts of both elements are not equal, it is impossible for String t to be an anagram of String s. In this case, return false.
2. Create an empty integer array `count`of size 26 to track frequencies. 'a' would represent 0 and 'z' would represent 26.
3. Loop over the Strings. For character c at index i:
a. s.charAt(i) should increase the count of that index in `count` by 1. 
b. t.charAt(i) should increase the count of that index in `count` by 1.
4. Finally, outside of the loop, check each element in `count`. If any frequencty is not 0, return false ( t is not an anagram of s).
5. Else, return true.

# Complexity
- Time complexity: O(n) 
(loops over all elements of both strings, so depends on the length of the strings).
<!-- Add your time complexity here, e.g. $$O(n)$$ --> 


- Space complexity: O(1)
(frequency array `count` will always be of length 26, irrespetive of the length of the strings).
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        int[] count = new int[26];
        for(int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for(int i : count){
            if (i != 0) return false;
        }

        return true;
    }
}
```