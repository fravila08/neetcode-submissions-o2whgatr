import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        # if len(s) < 2:
        #     return True 
        # if len(s) < 3 and s[0] != s[1]:
        #     return False
        left, right = 0, len(s)-1
        while left < right:
            if s[right] != s[left]:
                return False
            left += 1
            right -= 1
        return True