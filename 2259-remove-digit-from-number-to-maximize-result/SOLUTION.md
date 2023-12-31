##Logistics
Attempt Date: 31 December 2023 (backlog for 29 december)
|| Runtime: 1 ms Java (beat 76% of other submissions)
|| Memory: 41.4 MB Java (beat 39.55% other solutions)

## Intuition
The algorithm aims to remove a specific digit from a given number string while ensuring that the resulting number is the largest possible. To achieve this, the algorithm iterates through the input string and removes the first occurrence of the specified digit, considering the adjacent digits to maximize the resulting value.

## Approach
1. Initialize `last_index` to 0, representing the last index where the digit was removed.
2. Iterate through the characters of the input `number` starting from the second character (`i=1`).
    - Check if the previous character (`number.charAt(i-1)`) is equal to the target digit.
        - If true, compare the current character (`number.charAt(i)`) with the target digit.
            - If the current character is greater than the target digit, remove the digit at the previous index (`i-1`) to maximize the resulting number, and return the updated number.
            - Update `last_index` to `i-1` to keep track of the last removed digit index.
3. After the loop, check if the last character of the `number` is equal to the target digit.
    - If true, update `last_index` to the last index of the string.
4. Construct the result by concatenating the substrings before and after the `last_index`.

## Time Complexity
The algorithm iterates through each character in the input `number` once, resulting in a linear time complexity of O(N), where N is the length of the input string.

## Space Complexity
The algorithm uses a constant amount of space for variables (`last_index`, `len`, `i`). Therefore, the space complexity is O(1).

## Code
**Java**
```
class Solution {
    public String removeDigit(String number, char digit) {
        int last_index = 0;
        int len = number.length();

        for(int i = 1; i < len; i++) {
            if(number.charAt(i-1) == digit) {
                if(number.charAt(i) > digit) {
                    return number.substring(0,i-1) + number.substring(i, len);
                }
                last_index = i-1;
            }
        }

        if(number.charAt(len - 1) == digit) last_index = len - 1;

        return number.substring(0,last_index) + number.substring(last_index+1, len);
    }
}
```

**Python3**
```
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        index = 0

        for num in range(1, len(number)):
            if number[num-1] == digit:
                if int(number[num]) > int(number[num-1]):
                    # we have found the number to return
                    return number[:num-1] + number[num:]
                else:
                    index = num - 1

        if number[-1] == digit:
            index = len(number) - 1

        return number[:index] + number[index+1:]
```