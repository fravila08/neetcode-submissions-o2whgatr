class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)
            elif stack and pairs.get(stack[-1]) == char:
                stack.pop()
            else:
                return False
        return not stack
            
            
        