class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0
        while l < r:
            length = r - l
            curr_area = 0
            if heights[l] > heights[r]:
                curr_area = heights[r] * length
                r -= 1
            else:
                curr_area = heights[l] * length
                l += 1
            max_area = curr_area if max_area < curr_area else max_area
        return max_area

        