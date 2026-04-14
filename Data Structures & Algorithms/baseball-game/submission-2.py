class Stack:
    def __init__(self):
        self.base = []

    def addTop(self, val):
        self.base.append(val)

    def rmTop(self):
        self.base.pop() if self.base else None

    def peek(self):
        return self.base[-1] if self.base else None
    
    def sumStack(self):
        return sum(self.base)

    def addLastTwo(self):
        return self.base[-2] + self.base[-1] if len(self.base) >= 2 else None

    def doubleLast(self):
        return self.base[-1] * 2 if self.base else None

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        def is_num(val):
            try:
                int(val)
                return True
            except ValueError:
                return False

        stack = Stack()
        for op in operations:
            print("start", stack.peek())
            if is_num(op):
                stack.addTop(int(op))
            elif op == "+":
                val = stack.addLastTwo()
                if val:
                    stack.addTop(val)
            elif op == "D":
                val = stack.doubleLast()
                if val:
                    stack.addTop(val)
            else:
                stack.rmTop()
            print("end", stack.peek())
        return stack.sumStack()

        