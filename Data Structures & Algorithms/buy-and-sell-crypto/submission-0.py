class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices) - 1:
            if prices[left] > prices[right]:
                left = right
                right = left + 1
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                right += 1
                if profit > max_profit:
                    max_profit = profit 
        return max_profit