class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer: dict[str: list[str]] = {}
        for word in strs:
            ref = ''.join(sorted(word))
            answer[ref] = answer.get(ref, []) + [word]
        return list(answer.values())