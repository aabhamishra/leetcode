class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        # tracks indices of extra open parentheses
        stack = []

        for i in range(len(chars)):
            if chars[i] == "(":
                stack.append(i)
            elif chars[i] == ")":
                if stack:
                    stack.pop()
                else:
                    chars[i] = ""
        
        while stack:
            chars[stack.pop()] = ""

        return "".join(chars)
        