class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(r, c):
            if r == len(matrix):
                return 0
            if not (0  <= c < len(matrix[0])):
                return float("inf")
            ans = float("inf")
            for dx,  dy in [(1, 1), (1,0),(1, -1)]:
                ans = min(dp(r + dx, c + dy), ans)
            ans += matrix[r][c]
            return ans
        ans = float("inf")
        n = len(matrix[0])
        m = len(matrix)
        for i in range(n):
            ans = min(ans, dp(0, i))
        return ans