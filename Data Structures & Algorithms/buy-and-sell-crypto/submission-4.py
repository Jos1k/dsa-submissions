class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        profit = 0
        
        while r < len(prices):
            profit = max(profit, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l+=1
                if l == r:
                    r +=1
            else:
                r+=1

        return profit
