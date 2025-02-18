class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        for r in range(len(costs) - 2, -1, -1):
            for c in range(len(costs[0])):
                curr = costs[r][c]
                min_value = float("inf")
                for c2 in range(len(costs[0])):
                    if c2 != c:
                        min_value = min(min_value, costs[r + 1][c2])
                costs[r][c] = curr + min_value
        return min(costs[0])
#         @cache
#         def dp(row, prev):
#             if row == len(costs):
#                 return 0
            
#             return costs[row][prev] +  min(dp(row + 1, i) for i in range(len(costs[0])) if i != prev) 
    
#         return min(dp(0, i) for i in range(len(costs[0]))) 
            