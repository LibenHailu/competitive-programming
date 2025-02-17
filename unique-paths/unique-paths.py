class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dp(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            ans = 0
            if 0 <= r + 1 < m:
                ans += dp(r + 1, c)
            if 0 <= c + 1 < n:
                ans += dp(r, c + 1)
            return ans
        return dp(0, 0)