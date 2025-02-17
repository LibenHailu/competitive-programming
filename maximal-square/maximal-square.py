class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        @cache
        def dp(i, j):
            if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])):
                return 0
            if matrix[i][j] == '0':
                return 0
            return 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i+1, j+1))
        
        ans = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '1':
                    ans = max(dp(r, c)**2, ans)
        return ans