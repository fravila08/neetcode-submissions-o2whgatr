class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container_max = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            container_max = area if area > container_max else container_max
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return container_max