class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        key = {}
        for idx in range(len(numbers)):
            if numbers[idx] in key:
                return [key[numbers[idx]]+1, idx+1]
            key[target-numbers[idx]] = idx