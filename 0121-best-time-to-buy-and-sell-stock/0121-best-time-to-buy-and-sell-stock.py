class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MAX,low = 0,0
        for idx,price in enumerate(prices):
            if price-prices[low] < 0:
                low = idx
                print(f'update low = {low}, {price}')
            MAX = max(price-prices[low],MAX)
            print(f'MAX = {MAX}')
        return MAX