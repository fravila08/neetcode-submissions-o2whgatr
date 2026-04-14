class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for idx, ltr in enumerate(s):
            if ltr != t[idx]:
                return False
        return True
        