class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        while prices:
            anchor = prices[0]
            for price in prices[1:]:
                profit = max(profit, price-anchor)
            prices = prices[1:]
        return profit