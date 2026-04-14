import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        left, right = 0, len(s)-1
        while left < right:
            if s[right] != s[left]:
                return False
            left, right = left + 1, right - 1
        return True