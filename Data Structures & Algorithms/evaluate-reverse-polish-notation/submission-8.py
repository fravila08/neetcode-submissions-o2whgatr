import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda x, y: x+y,
            "*": lambda x, y: x*y,
            "/": lambda x, y: int(x/y),
            "-": lambda x, y: x-y,
        }

        stack = []

        for char in tokens:
            print(stack)
            if char in operations:
                #conduct math
                int2 = stack.pop()
                int1 = stack.pop()
                op = operations[char]
                stack.append(op(int1, int2))
            else:
                stack.append(int(char))
        print(stack)
        return stack[-1] or 0
        