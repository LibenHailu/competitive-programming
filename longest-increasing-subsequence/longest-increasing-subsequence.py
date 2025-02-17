class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = 1
        for i in range(len(nums) - 2, -1 , -1):
            max_val = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_val = max(max_val, dp[j])
            dp[i] = 1 + max_val
        return max(dp)