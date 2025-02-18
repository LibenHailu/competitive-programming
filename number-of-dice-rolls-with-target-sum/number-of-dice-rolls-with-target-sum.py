class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dp(n, target):
            if n == 0 and target == 0:
                return 1
            if  n == 0 or target < 0:
                return 0
            
            ans = 0
            for next_val in range(1, min(target + 1, k + 1)):
                ans += dp(n - 1, target - next_val) % MOD
            return ans % MOD
        return dp(n, target)
            
            
            