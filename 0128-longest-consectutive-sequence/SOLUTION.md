# Logistics
Attempt date: 27 December 2023

# Intuition
The question says that the solution must run in O(n) time. As the input array is unordered, simple iteration ovfer the array to find the longest sequence will be a problem. Using Arrays.sort is a simple solution but runs in O(nlogn) time. Hence, we neeed to think of another way to track consecutive elements. The data structure best capable for tracking unique elements is a Hashset, hence the following approach: 

<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
1. Intialize an integer `max` rto track to longest sequence length, and a HashSet that will contain all elements.
2. We add all elements from the input array to the HashSet `set`.
3. Next, let's iterate over the input array. For each element `num`:
-  We check if `num` is the start of a sequence i.e. if `set` contains `num-1`. If not, we know that `num` represents the start of a sequence. 
- In this case, we check the length of this sequence by looking for consecutive elements after `num`.
- When we fail to find the next element in the `set`, we then update `max` if the current sequence length is greater than it.
4. Lastly, we return max.


<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(n)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution {
    public int longestConsecutive(int[] nums) {
        int max = 0;
        Set<Integer> set = new HashSet();
        //populate the set with the input array
        for(int num : nums) set.add(num);

        //iterate through the input array, check if element denotes the start of a sequence
        for( int num : nums) {
            //start of sequence is found
            if(!set.contains(num-1)) {
                int length = 1;
                //check how many numbers are there in this sequence
                while(set.contains(num + length)) {
                    length++;
                }

                //update max length
                max = Math.max(max, length);
            }
        }

        return max;
    }
}
```