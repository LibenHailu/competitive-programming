class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp =  [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
#         memo = {}
#         def dp(n):
#             if n in memo:
#                 return memo[n]
#             if n == 0:
#                 return 1
#             if n < 0:
#                 return 0
#             ans = dp(n - 1) + dp(n - 2)
#             memo[n] = ans
#             return memo[n]
#         return dp(n)
        