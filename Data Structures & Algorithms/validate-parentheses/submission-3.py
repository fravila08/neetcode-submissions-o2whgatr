class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        opens = {"{", "(", "["}
        stack = []
        for char in s:
            if char in opens:
                stack.append(char)
            elif stack and pairs.get(stack[-1]) == char:
                stack.pop(-1)
            else:
                return False
        return not bool(stack)
            
            
        