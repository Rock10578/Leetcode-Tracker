class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MAX,low = 0,0
        for idx,price in enumerate(prices):
            if price-prices[low] < 0:
                low = idx
            MAX = max(price-prices[low],MAX)
        return MAX