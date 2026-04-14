class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        def product(ints:list[int]) -> int:
            prod = 1
            for num in ints:
                prod *= num
            return prod
        
        return [product(nums[:i]+nums[i+1:]) for i in range(len(nums))]
        