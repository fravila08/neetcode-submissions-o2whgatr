class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {} #key:code|val:list
        for word in strs:
            code = ''.join(sorted(word))
            res[code] = res.get(code, list()) + [word]
        return list(res.values())