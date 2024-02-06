class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for i in arr:
            # no-op
            if i == "." or i == "":
                continue
            # go up a level if level exists
            elif i == "..":
                if stack:
                    stack.pop()
            # file name encountered
            else:
                stack.append(i)
        
        return "/" + "/".join(stack)