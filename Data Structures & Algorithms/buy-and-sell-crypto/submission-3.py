class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        res = 0

        for p in prices:
            if p < buy_price:
                buy_price = p
            else:
                res = max(res, p - buy_price)
        
        return res
        