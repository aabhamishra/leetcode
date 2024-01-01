## Intuition
The algorithm aims to maximize the number of content children by distributing cookies with sizes represented by the array `s` to children with greed factors represented by the array `g`. It utilizes the two-pointer approach after sorting both arrays.

## Approach
1. Initialize `cookies` as the length of array `s`.
2. If `cookies` is 0, return 0 since there are no cookies to distribute.
3. Sort arrays `g` and `s` to facilitate the greedy assignment.
4. Initialize pointers `curr` and `content` to 0 to iterate through arrays `s` and `g`.
5. Iterate through the array `g` (children's greed factors).
	- While the size of the current cookie (`s[curr]`) is less than the current child's greed factor (`g[i]`):
		- Increment `curr` to consider the next cookie.
		- Check if `curr` reaches the end of array `s` (all cookies are used). If true, return the current content count.
	- Increment `content` since the current child is satisfied.
	- Increment `curr` to move to the next available cookie.
	- Check if `curr` reaches the end of array `s` (all cookies are used). If true, return the current content count.
6. Return the final content count.

## Time Complexity
The algorithm sorts both arrays `g` and `s`, which has a time complexity of O(N log N), where N is the length of the larger array. The iteration through the arrays has a linear time complexity of O(N), resulting in an overall time complexity of O(N log N).

## Space Complexity
The algorithm uses a constant amount of extra space, resulting in a space complexity of O(1).

## Code

**Java**
```
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int cookies = s.length;
        if (cookies == 0) return 0;

        Arrays.sort(g);
        Arrays.sort(s);

        int curr = 0;
        int content = 0;

        for (int i = 0; i < g.length; i++) {
            while (s[curr] < g[i]) {
                curr++;
                if (curr == cookies) return content;
            }

            content++;
            curr++;
            if (curr == cookies) return content;
        }

        return content;
    }
}
```

**Python3**

```
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0

        g.sort()
        s.sort()

        cookie, child = 0,0
        res = 0

        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                res+=1
                child+=1
            
            cookie+=1
        

        return res
        
```
