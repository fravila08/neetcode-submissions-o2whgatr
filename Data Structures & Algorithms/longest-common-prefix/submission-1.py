class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        point = strs[0]
        for idx in range(len(point)):
            for word in strs[1:]:
                if len(word)-1 < idx or word[idx] != point[idx]:
                    return res
            res += point[idx]
        return res