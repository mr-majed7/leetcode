class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        selected_prices = []
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                selected_prices.append(prices[i+1]-prices[i])
        return sum(selected_prices)