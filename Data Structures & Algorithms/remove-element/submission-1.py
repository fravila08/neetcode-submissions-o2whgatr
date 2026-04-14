class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_rm = list(filter(lambda x: x!=val, nums))
        for idx in range(len(nums_rm)):
            nums[idx] = nums_rm[idx]
        return len(nums_rm)
