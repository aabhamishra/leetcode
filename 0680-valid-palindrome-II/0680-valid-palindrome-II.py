class Solution:
    def validPalindrome(self, s: str) -> bool:

        def valid(string: str) -> bool:
            start = 0
            end = len(string) - 1

            while start < end:
                if string[start] != string[end]:
                    return False
                start+=1
                end-=1   
            return True
        
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return valid(s[start+1: end+1]) or valid(s[start:end])
            start+=1
            end-=1
        return True