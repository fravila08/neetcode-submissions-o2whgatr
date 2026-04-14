class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ''
        while word1 and word2:
            answer += word1[0]
            answer += word2[0]

            word1 = word1[1:]
            word2 = word2[1:]
        answer += word1 or word2
        return answer
        