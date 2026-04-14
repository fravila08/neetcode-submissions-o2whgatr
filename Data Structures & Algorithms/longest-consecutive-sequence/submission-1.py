class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        answer = 0
        seq = [nums[0]]
        for num in nums[1:]:
            if (seq[-1] + 1) == num:
                seq.append(num)
            elif seq[-1] == num:
                continue
            else:
                answer = len(seq) if len(seq) > answer else answer
                seq = [num]
        if seq:
            answer = len(seq) if len(seq) > answer else answer
        return answer