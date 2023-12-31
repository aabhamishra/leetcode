## Intuition
The algorithm aims to find the minimum consecutive sequence length of card values to be picked up from an array. 

Approach 1 entails using a sliding window, which takes up less memory but takes loger to run. It uses a sliding window approach with a HashSet to efficiently identify duplicates and track the minimum consecutive sequence length.

Approach 2 uses a HashMap instead. The hashmap tracks the indices of the elements encountered to identify duplicates. This approach uses more memory as compared to the first approach because it uses a HashMap instead of a HashSet. However, as we are iterating over each element twice in the worst case for approach 1, this aproach is faster. 

## Approach 1
1. Initialize variables `len` as the length of the `cards` array and `min` to `Integer.MAX_VALUE`.
2. Check if `len` is 1, and if true, return -1 as there is only one card.
3. Initialize `start` and `end` pointers to 0 for the sliding window.
4. Create a HashSet `set` to track unique card values in the current window.
5. Iterate through the `cards` array using the sliding window (`start` and `end`).
	- Check if the current card at `end` is already in the HashSet (`set`).
		- If true, a duplicate is found.
			- Iterate from `start` to the first occurrence of the duplicate, removing cards from the HashSet.
			- Update the minimum consecutive sequence length (`min`) based on the current window size.
			- Move the `start` pointer one step forward.
	- Move the `end` pointer one step forward.
6. Return the minimum consecutive sequence length (`min`) if it's not equal to `Integer.MAX_VALUE`, otherwise, return -1.

## Time Complexity
The algorithm iterates through each element in the `cards` array once or twice in the worst case, resulting in a linear time complexity of O(N), where N is the length of the array.

## Space Complexity
The algorithm uses a HashSet (`set`) to store unique cards within the sliding window. In the worst case, the HashSet may store all distinct cards, leading to a space complexity of O(N), where N is the length of the array.

## Code
```java
class Solution {
    public int minimumCardPickup(int[] cards) {
        int len = cards.length;
        int min = Integer.MAX_VALUE;

        if (len == 1) return -1;

        int start = 0;
        int end = 0;

        Set<Integer> set = new HashSet();

        while (end < len) {
            if (!set.add(cards[end])) {
                int dupl = cards[end];
                while (cards[start] != dupl) {
                    set.remove(cards[start]);
                    start++;
                }
                min = Math.min(min, end - start + 1);
                start++;
            }
            end++;
        }

        return min == Integer.MAX_VALUE ? -1 : min;
    }
}
```

## Approach 2:
1. Initialize `min` to `Integer.MAX_VALUE` as the placeholder for the minimum consecutive sequence length.
2. Create a HashMap `map` to store the last index of each card value encountered.
3. Iterate through the `cards` array.
	- Check if the current card at index `i` is already in the HashMap `map`.
		- If true, update `min` based on the current consecutive sequence length (`i - map.get(cards[i]) + 1`).
	- Update the last index of the current card in the HashMap `map`.
4. Return `min` if it's not equal to `Integer.MAX_VALUE`, otherwise, return -1.

## Time Complexity
The algorithm iterates through each element in the `cards` array once, resulting in a linear time complexity of O(N), where N is the length of the array.

## Space Complexity
The algorithm uses a HashMap (`map`) to store the last index of each card value. In the worst case, the HashMap may store all distinct cards, leading to a space complexity of O(N), where N is the length of the array.


## Code

```
class Solution {
    public int minimumCardPickup(int[] cards) {
        
        int min = Integer.MAX_VALUE;
        HashMap<Integer, Integer> map = new HashMap();
        
        for( int i = 0; i < cards.length; i++) {
            if(map.containsKey(cards[i])) {
                min = Math.min(min, i - map.get(cards[i]) + 1);
            }

            map.put(cards[i], i);
        }
        
        return min == Integer.MAX_VALUE ? -1 : min;
    }
}
```