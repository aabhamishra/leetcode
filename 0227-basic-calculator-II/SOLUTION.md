## Intuition
The problem involves evaluating a string containing arithmetic expressions with addition, subtraction, multiplication, and division operations.

The algorithm efficiently evaluates arithmetic expressions by leveraging a stack-based approach. It first processes division and multiplication operations and then handles addition and subtraction operations. By iteratively evaluating numeric tokens and operations, it computes the final result of the expression.

## Approach

The algorithm evaluates the expression by first calculating all division and multiplication operations, and then performing addition and subtraction operations.

1. **Stack-based Evaluation**: Initialize an empty stack to store intermediate results. Iterate through the string character by character.

2. **Numeric Token Processing**: If the current character is numeric, extract the entire numeric token and convert it to an integer. Push the integer onto the stack. If an operation is pending (e.g., division or multiplication), perform the operation before pushing the integer onto the stack.
3. **Operation Processing**: If the current character is an arithmetic operation (`+`, `-`, `*`, `/`), store it in the `operation` variable for future use.
4. **Result Calculation**: After processing all tokens, iterate through the stack and perform any remaining addition and subtraction operations to obtain the final result.

The algorithm returns the result of evaluating the arithmetic expression.

## Complexity
- Time complexity:
The time complexity is O(N), where N is the length of the input string `s`. The algorithm iterates through each character of the string once.

- Space complexity:
The space complexity is O(N), where N is the length of the input string `s`. The algorithm uses additional space for the stack to store intermediate results.

## Code
```python
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
```