class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = 0
        water = 0
        for i in range(1, len(height)):

            if height[i] < height[i-1] and height[start] <= height[i-1]:
                start = i - 1
            elif height[start] <= height[i]:
                end = i
                if end - start > 1:
            
                    bar = min(height[start], height[end])
                    left = start + 1
                    right = end
                    while left < right:
                        
                        water +=  bar - height[left]
                        left += 1
        return water