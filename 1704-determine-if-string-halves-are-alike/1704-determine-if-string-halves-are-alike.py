class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        diff = 0
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while start < end:
            if s[start] in vowels:
                diff+=1
            if s[end] in vowels:
                diff-=1
            
            start+=1
            end-=1
        
        return diff == 0 