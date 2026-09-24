class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1

        while left != right:
            width = right - left
            height = min(heights[left], heights[right])
            print(width)
            print(height)
            if width == height:
                return width*height
            elif  width <  height:
                right -= 1
            else:
                left += 1
            