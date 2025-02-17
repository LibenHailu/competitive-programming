class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, highest = float("inf"), float("-inf")
        ans = 0
        for price in prices:
            if price < lowest:
                lowest = price
                highest = price
            if price > highest:
                highest = price
                ans = max(ans, highest - lowest)
        return ans