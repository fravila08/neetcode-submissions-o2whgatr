class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key = {}
        for idx, num in enumerate(nums):
            if num in key:
                return [key[num], idx]
            key[target-num] = idx
        