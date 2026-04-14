class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for idx, num in enumerate(nums):
            if num in map:
                return [map[num], idx]
            else:
                map[target - num] = idx
