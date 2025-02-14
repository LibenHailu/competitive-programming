class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0

        ans = 0
        ans += self.climbStairs(n - 1)
        ans += self.climbStairs(n - 2)
        return ans