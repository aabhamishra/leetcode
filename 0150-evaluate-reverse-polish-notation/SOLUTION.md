# Intuition
Reverse Polish Notation (RPN) allows for evaluating expressions without parentheses due to its postfix structure. It processes operands first, followed by operators.

A stack is ideal for managing this order as it maintains the correct operand sequence for computations.

# Approach
1. Initialize a stack to store operands.
2. Iterate through the tokens:
    - If a token is an operand, push it onto the stack.
    - If a token is an operator:
        - Pop the top two operands from the stack (op2, op1).
        - Perform the operation based on the operator.
        - Push the result back onto the stack.
3. The final result will be the last element in the stack.

# Complexity
- Time complexity: $O(n)$
Each token is processed once, involving constant-time operations.

- Space complexity: $O(n)$
Primarily due to the stack. In the worst case, all tokens are operands, requiring storage in the stack.



This Python code implements the described approach using a list for the stack and a dictionary to identify operators for efficiency. 
# Code
```
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"}
        
        for s in tokens:
            if s in operands:
                # we have found an operator. calculate expression
                op2 = stack.pop()
                op1 = stack.pop()

                if s == "+":
                    stack.append(op1 + op2)
                elif s == "-":
                    stack.append(op1 - op2)
                elif s == "*":
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 / op2))
            else:
                # we have an operand
                stack.append(int(s))

        # end result is stored in stack after last operation.
        return stack.pop()

```