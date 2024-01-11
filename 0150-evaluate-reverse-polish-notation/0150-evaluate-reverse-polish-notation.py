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