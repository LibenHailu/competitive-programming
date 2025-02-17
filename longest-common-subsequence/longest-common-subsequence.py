class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         @cache
#         def dp(index1, index2):
#             if index1 == len(text1) or index2 == len(text2):
#                 return 0
            
#             if text1[index1] == text2[index2]:
#                 return 1 + dp(index1 + 1, index2 + 1)
#             else:
#                 return max(dp(index1 + 1, index2), dp(index1, index2 + 1))
#         return dp(0, 0)
        memo = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        
        for r in range(len(text2) - 1, -1, -1):
            for c in range(len(text1)- 1, -1, -1):
                if text1[c] == text2[r]:
                    memo[r][c] = 1 + memo[r + 1][c + 1]
                else:
                    memo[r][c] = max(memo[r][c + 1], memo[r + 1][c])
        return memo[0][0]