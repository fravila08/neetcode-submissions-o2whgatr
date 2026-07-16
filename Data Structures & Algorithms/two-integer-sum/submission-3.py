class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff not in hmap:
                hmap[nums[idx]] = idx
            else:
                return [hmap[diff], idx]