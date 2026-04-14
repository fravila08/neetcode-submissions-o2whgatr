class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer: dict[str: list[str]] = {}
        for word in strs:
            ref = ''.join(sorted(word))
            if ref in answer:
                answer[ref].append(word)
            else:
                answer[ref] = [word]
        print(list(answer.values()))
        return list(answer.values())