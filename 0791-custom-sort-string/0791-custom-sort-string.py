class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map = {}

        for c in s:
            map[c] = map.get(c, "") + c
        
        s = ""

        for c in order:
            if c in map:
                s += map[c]
                del map[c]
        
        for left_char in map:
            s += map[left_char]
        
        return s