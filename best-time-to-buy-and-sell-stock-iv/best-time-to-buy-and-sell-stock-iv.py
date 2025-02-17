class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, remaining, holding):
            if i == len(prices) or remaining == 0:
                return 0
            
            do_nothing = dp(i + 1, remaining, holding)
            do_something = 0
            if holding:
                do_something = prices[i] + dp(i + 1, remaining - 1, 0)
            else:
                do_something = -prices[i] + dp(i + 1, remaining, 1)
            
            return max(do_nothing, do_something)
        return dp(0, k, 0)
    
    