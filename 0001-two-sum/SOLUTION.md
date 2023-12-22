# Logistics
Attempt date: 21 December 2023
Runtime: 1 ms
Memory Usage: 44.2 MB

# Intuition
We need to keep track of the the values present in the array as well as the index of each value (which is what we need to return). To store two values, and knowing that there is only one unique answer, we can successfully use a HashMap.


# Approach
1. Create an empty HashMap with <key, value> as <Integer, Integer>. 
    keys = array elements, values = indices.
2. Loop over the array: 
    - If the HashMap already contains the difference (target - current element), this means we have found our result. Return a new array with the index of the array, and the key value associated with the "difference" number.
    - Else, we should add the element and its associated index in the array to the HashMap.
3. Outside the loop, just return a new empty array. As we have one guarantedd solution, this line will never be executed.

# Complexity
- Time complexity: O(n)
Time complexity depends on the size of the array as its elements are being iterated on. Hashtable has average O(1) complexity for add and lookup.

- Space complexity: O(n)
HashMap takes O(n) space. 

# Code
```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) return new int[]{i, map.get(target - nums[i])};
            map.put(nums[i], i);
        }

        return new int[2];
    }
}
```