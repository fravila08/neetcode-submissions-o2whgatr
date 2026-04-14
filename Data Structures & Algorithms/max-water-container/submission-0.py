class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container_max = 0
        l, r = 0, len(heights)-1
        while l < r:
            area_height = min(heights[l], heights[r])
            area_width = r - l
            area = area_width * area_height
            if area > container_max:
                container_max = area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return container_max