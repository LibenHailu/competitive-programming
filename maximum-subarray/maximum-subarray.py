class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runnigsum = 0
        maxSum = float("-inf")
        for num in nums:
            if runnigsum < 0:
                runnigsum = num
            else:
                runnigsum += num
            maxSum = max(maxSum, runnigsum)
        return maxSum
        