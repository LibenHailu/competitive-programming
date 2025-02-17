class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @cache
        def dp(i, j, k):
            if i > j or k == len(multipliers):
                return 0
            return max(nums[i] * multipliers[k] + dp(i + 1, j, k + 1),nums[j] * multipliers[k] + dp(i, j - 1, k + 1))
        return dp(0, len(nums) - 1, 0)