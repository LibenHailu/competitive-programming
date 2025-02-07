class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        ans = float("inf")
        left, right = 0, 1
        while left < right and right < len(prefix):
            if prefix[right] - prefix[left] >= target:
                ans = min(right - left, ans)
                left += 1
            else:
                right += 1
        
        # ans = float("inf")
        
        # for i in range(1, len(prefix)):
        #     for j in range(i, len(prefix)):
        #         if prefix[j] - prefix[i - 1] >= target:
        #             ans = min(j - i + 1, ans)
        return ans if ans != float("inf") else 0
                    