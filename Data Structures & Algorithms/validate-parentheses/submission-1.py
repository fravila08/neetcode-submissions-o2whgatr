class Stack:
    def __init__(self):
        self.base = []
    
    def push(self, val):
        self.base.append(val)

    def pop(self):
        self.base.pop(-1)

    def peek(self):
        return self.base[-1] if self.base else None

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        legend = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for char in s:
            print(stack.base)
            if char in legend.keys():
                stack.push(char)
            elif legend.get(stack.peek(), None) == char:
                stack.pop()
            else:
                return False
        return not stack.base
            

        