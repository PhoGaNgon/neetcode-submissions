class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lowest_left = [0] * n
        highest_right = [0] * n

        lowest_left[0] = prices[0]
        highest_right[n - 1] = prices[n - 1]
        for i in range(1, n):
            lowest_left[i] = min(lowest_left[i - 1], prices[i])

        for i in range(n - 2, -1, -1):
            highest_right[i] = max(highest_right[i + 1], prices[i])

        res = 0
        for i in range(n):
            res = max(res, highest_right[i] - lowest_left[i])
        
        return res
        