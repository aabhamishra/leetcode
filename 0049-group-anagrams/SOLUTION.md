# Logistics
Attempt date: 22 December 2023
Runtime: 6 ms
Memory Usage: 46.9 MB

# Intuition
Considering we have to return a list of anagram lists, we have to keep track of each unique anagram and the strings associated with that anagram. The easiet way of checking if one string is an anagram of the other is by arranging the lettters of each string in alphabetical order and then using the `String.equals()` method to compare the two.

For this particular question, let's keep track of the lists using a HashMap. This is best because lookup and addition is fastest - O(1) -  in HashMaps.


# Approach
1. Create a new `HashMap<String, List<String>> groups` to track the individual lists. The key stores an alphabetically ordered version of the anagram strings. The value contains a list of strings that are anagrams of the key string.
2. Loop over each string `str` in the input array.
    - Covert the string to a character array. Sort the array. Finally convert this ordered array to an ordered string - `sAlpha`.
    - From `groups`, retrieve the list associated with sAlpha if it exists, or create a new list. 
    - Add `str` to the list, and add the new pair to the HashMap. 
3. Finally return an arraylist created by the list of values in `groups` using `HashMap.values()`.

# Complexity
- Time complexity: **O(n*klog(k))**
The outer iteration is over the array, which depends on the number of elements - O(n). Inside the loop, the dominant execution is the character array being ordered alphabetically, which takes klog(k) time where k is the length of the array. Multiplying the two, we get the above time complexity. 


# Code
```
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> groups = new HashMap<>();
        for( String s : strs ) {
            char[] sArr = s.toCharArray();
            Arrays.sort(sArr);
            String sAlpha = String.valueOf(sArr);

            List<String> list = groups.getOrDefault(sAlpha, new ArrayList<String>());
            list.add(s);
            groups.put(sAlpha, list);
        } 

        return new ArrayList<>(groups.values());
    }
}
```