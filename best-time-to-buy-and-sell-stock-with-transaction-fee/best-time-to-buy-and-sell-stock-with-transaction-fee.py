class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, holding):
            if i == len(prices) and not holding:
                return 0
            if i == len(prices):
                return float("-inf")
            do_nothing = dp(i + 1, holding)
            do_something = 0
            if holding:
                do_something =  prices[i] + dp(i + 1, 0)
            else:
                do_something = -prices[i] + dp(i + 1, 1) - fee
            
            return max(do_nothing, do_something)
        return dp(0, 0) 
            
            