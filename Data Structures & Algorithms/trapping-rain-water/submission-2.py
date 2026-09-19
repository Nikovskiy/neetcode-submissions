class Solution:
    def trap(self, height: List[int]) -> int:
            
        n = len(height)
        if n == 0:
            return 0

        water = 0

        start = 0
        for i in range(1, n):
            if height[i] >= height[start]:
                bar = height[start]
                for j in range(start + 1, i):
                    water += bar - height[j]
                start = i


        end = n - 1
        for i in range(n - 2, start - 1, -1):
            if height[i] >= height[end]:
                bar = height[end]
                for j in range(i + 1, end):
                    water += bar - height[j]
                end = i

        return water