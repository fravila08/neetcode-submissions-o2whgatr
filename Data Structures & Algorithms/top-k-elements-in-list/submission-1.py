class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key = {}
        for num in nums:
            key[num] = key.get(num, 0) + 1
        answer = []
        for num, count in sorted(key.items(), key=lambda x:x[1], reverse=True):
            answer.append(num)
            if len(answer) == k:
                return answer
        