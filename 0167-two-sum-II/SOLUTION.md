# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The original two sum problem, the input array had to first be stored to Hash map. This was done so that retrieval and checks could be done in O(1) time. In this situation, however, the array is already sorted. This means that we can retrieve the indices of the two elements without having to add elements to a HashMap first.

The approach we use is that of two pointers: `start` and `end`, initialized to the first and last index of the `numbers` array. 

The idea is that as the array is sorted, start will point to the smallest element, and end will point to the largest element. 

When we check if `val = numbers[start] + numbers[end]` equals `target`, there are only three possibilities:

1. `val > target`: as there is no smaller element than `numbers[start]` but we have to reduce the sum to reach the target, we should move to the element smaller than `numbers[end]`.
2. `val < target`: as there is no bigger element than `numbers[end]` but we have to increase the sum to reach the target, we should move to the element bigger than `numbers[start]`.
3. `val = target`: we have found the correct elements and just return their 1-indexed indices!

The loop should run only till all elements have been accessed, i.e. while `start < end`.

# Approach
1. Intialize start and end pointers to 0 and len(numbers) - 1.
2. While (start < end)
- Appoint the sum of numbers[start] and numbers[end] to a variable `val`.
- If val is less than target, we increase start by 1. 
- Else if val is greater than target, we decrease end by 1.
- Else, this measn we have found the right elements, and we return a new array [start+1, end+1] (instead of [start, end] as the array is 1-indexed).
- Outside of the loop, return a new array [-1,-1] - this statement will never be executed as each test case is guaranteed  to have a solution.

# Complexity
- Time complexity: O(n)
Only one pass over the array
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
Jut a couple varibales defined as auxiliary space.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code - Python
```
class Solution(object):
    def twoSum(self, numbers, target):

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        start, end = 0, len(numbers) - 1

        while start < end:
            val = numbers[start] + numbers[end]

            if val < target:
                start+=1
            elif val > target:
                end-=1  
            else: 
                return [start+1, end+1]
                
        return [-1,-1]
        
```

# Code - Java

```
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length - 1;

        while (start < end){
            if(numbers[start] + numbers[end] == target) return new int []{start+1, end+1};

            if(numbers[start] + numbers[end] < target) start++;
            else end--;
        }

        return new int[]{0,0};
    }
}
```