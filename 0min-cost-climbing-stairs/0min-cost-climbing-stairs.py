class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # N = len(cost)
        # memo = cost[:]
        # memo.append(0)
        # for i in range(2, N + 1):
        #     memo[i] += min(memo[i - 1], memo[i - 2]) 
        # return memo[N]
        @lru_cache(None)
        def dp(i):
            if i >= len(cost):
                return 0
            
            return cost[i] + min(dp(i + 1), dp(i + 2))
        
        return min(dp(0), dp(1))