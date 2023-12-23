# [1496. Path Crossing](https://leetcode.com/problems/path-crossing/description/?envType=daily-question&envId=2023-12-23)

Given a string `path`, where `path[i] = 'N'`, `'S'`, `'E'` or `'W'`, each representing moving one unit north, south, east, or west, respectively. You start at the origin `(0, 0)` on a 2D plane and walk on the path specified by `path`.

Return `true` if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return `false` otherwise.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123929-pm.png" style="width: 400px; height: 358px;">

```
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123843-pm.png" style="width: 400px; height: 339px;">

```
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.```

**Constraints:** 

- `1 <= path.length <= 10^4`
- `path[i]` is either `'N'`, `'S'`, `'E'`, or `'W'`.