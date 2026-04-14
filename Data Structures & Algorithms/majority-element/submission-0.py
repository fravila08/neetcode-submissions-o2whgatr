class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        marker = len(nums)//2
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter.get(num) > marker:
                return num
        return -1