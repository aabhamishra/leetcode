class Solution:
    def calculate(self, s: str) -> int:
        # first calculate all / and *
        # then calculate all additions and subtractions

        stack = []
        curr = 0
        operation = ""

        while curr < len(s):
            if s[curr].isnumeric():
                num_str = ""
                while curr < len(s) and s[curr].isnumeric():
                    num_str += s[curr]
                    curr += 1
                
                num = int(num_str)

                if operation == "":
                    stack.append(num)
                else:
                    if operation == "/":
                        stack.append(int(stack.pop() / num))
                    elif operation == "*":
                        stack.append(stack.pop() * num)
                    elif operation == "-":
                        stack.append(num * -1)
                    else:
                        stack.append(num)
                    
                operation = ""
                num = 0

            elif s[curr] in {"+", "-", "*", "/"}:
                operation = s[curr]
                curr+=1
            
            else:
                curr +=1

        res = 0 
        while stack:
            res += stack.pop()
        
        return res