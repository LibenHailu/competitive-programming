class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(r, c):
            if r == len(obstacleGrid) - 1  and c == len(obstacleGrid[0]) - 1 and obstacleGrid[r][c] != 1:
                return 1
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            ans = 0
            if 0 <= r + 1 < len(obstacleGrid):
                ans += dp(r + 1, c)
            if 0 <= c + 1 < len(obstacleGrid[0]):
                ans += dp(r, c + 1)
            return ans
        return dp(0, 0)