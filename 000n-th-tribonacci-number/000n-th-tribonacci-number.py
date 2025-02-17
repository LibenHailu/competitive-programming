class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # if n < 3:
        #     return 1
        # memo = [0] * (n + 1)
        # memo[0] = 0
        # memo[1] = 1
        # memo[2] = 1
        # for i in range(3, n + 1):
        #     memo[i] = memo[i - 3] + memo[i - 2] + memo[i - 1]
        # return memo[n]
        
        if n == 0:
            return 0
        if n < 3:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)