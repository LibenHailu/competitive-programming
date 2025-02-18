class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        @cache
        def dp(row, prev):
            if row == len(costs):
                return 0
            
            return costs[row][prev] +  min(dp(row + 1, i) for i in range(len(costs[0])) if i != prev) 
    
        return min(dp(0, i) for i in range(len(costs[0]))) 