## Intuition
We need to check if the abbreiation matches the word. This means that we need to track elements of both strings at the same time. The soluton hence calls for a two pointer solution (albeit one pointer per string).

- `word_p` tracks the word
- `abbr_p` tracks the abbreviation

We iterate over the strings while both of the pointers are within their respective string length limits, and check for inconsistencies described below in the approach.

## Approach
1. **Initialization:**
   - Initialize two pointers, `word_p` for the word and `abbr_p` for the abbreviation, both starting at the beginning.
2. **Iteration:**
   - Iterate through the characters of the abbreviation and word.
     - If the abbreviation character is a letter:
       - Check for a match with the corresponding word character.
       - If there is no match, return `False`.
       - Otherwise, increment both `abbr_p` and `word_p` by 1.
     - If the abbreviation character is numeric:
       - Extract the number from the abbreviation.
       - If `num` is '0', return `False`.
       - Extract the complete numeric part from the abbreviation and increment `abbr_p` accordingly.
       - Skip the corresponding number of characters in the word by incrementing `word_p` by `int(num)`.

3. **Final Check:**
   - After the iteration, check if both pointers reach the end of their respective strings.
   - If one pointer reached the end while the other did not, return `False`.

4. **Result:**
   - Return `True` if the word matches the abbreviation; otherwise, return `False`.
## Complexity
- Time complexity: $O(A)$
We check each element in the abbreviation exactly once. The operations in eah iteration take O(1) time and so the time complexity of the whole algorithm is O(A) where A is the length of the abbreviation.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
We use constant space to store the values of the two pointers.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_p = 0
        abbr_p = 0

        while abbr_p < len(abbr) and word_p < len(word):
            if abbr[abbr_p].isalpha():
                if word[word_p] != abbr[abbr_p]:
                    return False
                abbr_p+=1
                word_p+=1
            else:
                num = abbr[abbr_p]
                if num == '0':
                    return False
                
                abbr_p += 1
            
                while abbr_p < len(abbr) and abbr[abbr_p].isnumeric():
                    num += abbr[abbr_p]
                    abbr_p+=1
                
                word_p+= int(num)
        
        return word_p == len(word) and abbr_p == len(abbr)

```