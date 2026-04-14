# class Stack:
#     def __init__(self):
#         self.base = []
    
#     def push(self, val):
#         self.base.append(val)

#     def pop(self):
#         self.base.pop(-1)

#     def peek(self):
#         return self.base[-1] if self.base else None

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        legend = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for char in s:
            if char in legend.keys(): #is the char an opening bracket
                stack.append(char) # add to the stack (LAST IN)
            elif legend.get(stack[-1] if stack else None, None) == char: 
                # a closing char, we will match the LAST element in the stack to ensure we have
                # opening and closing brackets of the same type
                stack.pop(-1) # remove from the top of the stack (FIRST OUT)
            else: # string is unbalanced and we could kill the function early by returning False
                return False
        return not stack # if the stack is empty the string is balanced else unbalanced
            

        