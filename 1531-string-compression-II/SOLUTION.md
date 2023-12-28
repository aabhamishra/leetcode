# LeetCode String Compression II

## Logistics:

Attempt Date: 28 December 2023
|| Runtime: 3979ms (beat 100% submissions)
|| Memory: 69.5 mb (beat 100% submissions)

## Intuition:

The problem requires finding the minimum length of the compressed string after performing at most `k` removals from the original string `s`. This can be solved using dynamic programming. 

The idea is to define a recursive function that considers two options at each step: either keep the current character and continue the sequence, or delete the current character and move on to the next one. The function should keep track of the number of removals left (`k`), the previous character, and the count of consecutive occurrences of the previous character.

## Approach:

1. Define a recursive function `count(i, k, prev, prev_count)` that takes the current index `i`, the number of removals left `k`, the previous character `prev`, and the count of consecutive occurrences of the previous character `prev_count`.
2. Check three base cases:
   - If the current state has already been executed, return the stored result.
   - If the number of removals is negative, return infinity to discard this option.
   - If the end of the string is reached (`i == len(s)`), return 0 as no more characters need to be processed.
3. Handle recursive cases:
   - If the current character is the same as the previous character (`s[i] == prev`), calculate the increment (`incr`) based on whether the current run-length encoding will increase in length. Recursively call the function for the next element with an updated count (`prev_count+1`).
   - If the current character is different from the previous character, calculate the minimum length by considering two options: (A) delete the current character and recursively call for the next element with reduced removals (`k-1`), and (B) keep the current character as a new sequence and recursively call for the next element with the count reset to 1.
4. Store the result in the `executed` hashmap to avoid redundant calculations and return the result.

## Time Complexity:

The time complexity of this solution is O(n^2 * k). This is because the unique number of times the function count will run is based on its inputs (i, k, prev, prev_count). 

i: (0 -> n) hence n unique values
k: (0 -> k) hence k unique values
prev: (0 -> 26) hence 26 unique values
prev_count: (0 -> n) hence n unique values.

Based on these input combination possibilities, program will run in O(n^2*k) time.



## Space complexity: 

Similar to the time complexity, the hashmap `executed` will store O(n^2 * k) solutions. 

# Code
```
class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        # hashmap of counts already executed
        executed = {}

        # counts the minimum length of optimal compression 
        # i = current index
        # k = removals left
        # prev = character at i-1 index
        # prev_count = number of consecutive "prev" characters before i
        def count(i, k, prev, prev_count):
            # 3 base cases below:
            # 1. if this count is already calculated, just return
            if (i, k, prev, prev_count) in executed:
                return executed[(i, k, prev, prev_count)]
            # 2. if removals exceed what can be executed, return inf so that this iteration is dismissed
            if k < 0:
                return float("inf")
            # 3. if i reaches end of string
            if i == len(s): 
                return 0

            # recursive cases: 
            # 1. if current element equals previous
            if s[i] == prev:
                # check if this rle encoding will increase in length. this only happens for below previous counts 
                incr = 1 if prev_count in [1,9,99,9999,99999] else 0   
                # return recursive call for next element
                res = incr + count(i+1,k,s[i], prev_count+1)
            # 2. if current element does not equal previous aka new sequence is being started
            else:
                # return minimum of count if : (A) s[i] is deleted and (B) s[i] is kept
                res = min(
                    count(i+1, k-1, prev, prev_count), # s[i] deleted
                    1 + count(i+1, k, s[i], 1) # s[i] kept
                )
            
            executed[(i, k, prev, prev_count)] = res
            return res
        return count(0, k, "", 0)        

        """
        :type s: str
        :type k: int
        :rtype: int
        """


        
```