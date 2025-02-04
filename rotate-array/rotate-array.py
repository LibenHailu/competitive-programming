class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        updated =  [0] * len(nums)
        for i in range(len(nums)):
            updated[(i + k) % len(nums)] = nums[i]
        nums[:] = updated