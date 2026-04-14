class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            item = nums[i]
            j = i-1
            while j >= 0 and item < nums[j] :
                    nums[j + 1] = nums[j]
                    j -= 1
            nums[j + 1] = item
        return nums
