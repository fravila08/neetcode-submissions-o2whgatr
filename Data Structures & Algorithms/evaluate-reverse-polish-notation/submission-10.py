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
            if char in operations:
                int2 = stack.pop()
                int1 = stack.pop()
                stack.append(operations[char](int1, int2))
            else:
                stack.append(int(char))
        return stack[-1]
        