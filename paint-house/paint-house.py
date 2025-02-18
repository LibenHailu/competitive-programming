class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(row, prev):
            if row == len(costs):
                return 0
            
            ans = float("inf")
            ans = min(ans, dp(row + 1, (prev + 1) % 3))
            ans = min(ans, dp(row + 1, (prev - 1) % 3))
            ans += costs[row][prev]
            return ans 
    
        ans = float("inf")
        for i in range(len(costs[0])):
            ans = min(dp(0, 0),dp(0, 1),dp(0, 2))
        return ans 