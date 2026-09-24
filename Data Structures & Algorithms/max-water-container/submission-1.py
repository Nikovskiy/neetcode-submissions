class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_water = 0
        while left != right:
            width = right - left
            height = min(heights[left], heights[right])
            water = width*height
            if water > max_water:
                max_water = water
            if  width <  height:
                right -= 1
            else:
                left += 1
        return max_water
            