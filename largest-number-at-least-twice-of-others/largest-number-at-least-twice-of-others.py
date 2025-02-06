class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxValue = max(nums)
        i = nums.index(maxValue)
        for idx, num in enumerate(nums):
            if idx == i:
                continue
            if num * 2 > maxValue:
                return -1
        return i