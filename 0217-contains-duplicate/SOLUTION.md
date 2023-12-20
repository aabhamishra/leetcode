# Logistics
Attempt date: 20 December 2023
Runtime: 10 ms
Memory Usage: 54.6 MB

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
While searching for duplicates, hashset is the immediate 
first choice because of reduced lookup time complexity.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Create an empty hash set with an Integer type. 
2. Loop over each element in the array. If the hashset already contains this element, return `true`. Else, add the element to the set.
3. After the loop, return `false`, as this depicts the case that all elements have been looped over without finding any duplicates.


# Complexity
- Time complexity: O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
- Space complexity: O(n)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->


# Code
```
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet set = new HashSet<Integer>();
        for(int i : nums) {
            if(set.contains(i)) return true;
            set.add(i);
        }

        return false;
    }
}
```​