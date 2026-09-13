class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_water = 0
        while left < right:
            
            width = right - left
            height = min(heights[left], heights[right])
            water = width*height

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            if max_water < water:
                max_water = water
        return max_water
            