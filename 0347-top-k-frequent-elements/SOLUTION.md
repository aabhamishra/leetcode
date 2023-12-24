# Logistics
Attempt date: 24 December 2023
Runtime: 10 ms
Memory Usage: 48.2 MB

# Intuition
The questions asks us to find the top K elements with hightest frequency of occurance in the input array. The first step to this problem is to map each unique element in the input array to its frequency of occurence. Using a HashMap for this is best because of fastest additions and lookups. Lets call this HashMap `frequencies`.

Now that we have this hashmap, our next step shpould be to somehow map the frequencies to elements. This would allow us to find the top K elements with the highest frequencies. Although we have to 'map' these values, we cannot use a hashmap as multiple elements can have the same frequncy with which they occur in the array.

To solve this part of the problem, let's use a bucket list. For this problem, it should be an array os arraylists, where each index in the array represents a frequency. The arraylist at a specific index consists of the elements from the input array that occur at that frequency. The bucket list should contain frequencies 0 -> length of input array (as if every element in the input array was the same, the highest frequency needed would be the length of the input array)

Finally, we iterate through the bucket list (from highest index going down to 0) and add the top k elements to a return array. 

<!-- Describe your first thoughts on how to solve this problem. -->
# Approach
1. Initialize an empty HashMap<Integer, Integer> `freq`
2. Iterate over `nums` (the input array) and update element -> frequency pairs in `freq`.
3. Now, create an array of ArrayLists `bucketList` of size `nums.length`and intialize each element as an empty ArrayList.
4. Iterate over each entry in `freq` and for each value (frequency), add the key (element) to the arraylist associated with the frequency's index in `bucketlist`.
5. Finally, initialize an array `topk` which is the array to return. 
6. Iterate over `bucketlist` from highest index to 0, and add the top k elements to this array. Keep a counter to track the elements added.
7. Return `topk`!
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //HashMap that maps number -> its frequency
        Map<Integer, Integer> freq = new HashMap();
        for(int num : nums) freq.put(num, freq.getOrDefault(num, 0) + 1);

        //Array that contains a list of numbers with frequency equal to that index of the array
        List<Integer>[] bucketList = new ArrayList[nums.length + 1];
        for(int i = 0; i <= nums.length; i++) bucketList[i] = new ArrayList<Integer>();

        for(HashMap.Entry<Integer, Integer> e : freq.entrySet()) {
            bucketList[e.getValue()].add(e.getKey()); 
        }

        //Array with the top k frequencies.
        int[] topK = new int[k];
        for(int i = nums.length; i >=0; i--) {
            if(bucketList[i].size() > 0) {
                for(int n : bucketList[i]) {
                    topK[k-1] = n;
                    k--;
                    if(k == 0) return topK;
                }
            }
        }

        return topK;
    }
}
```