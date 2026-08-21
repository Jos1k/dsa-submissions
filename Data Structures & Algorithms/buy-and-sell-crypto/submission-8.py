class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_b = prices[0]
        max_p = 0
        for price in prices:
            max_p = max(price - min_b, max_p)
            min_b = min(min_b, price)

        return max_p