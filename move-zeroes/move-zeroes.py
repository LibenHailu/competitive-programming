class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                cur = i
                while cur < len(nums):
                    if nums[cur] != 0:
                        nums[i], nums[cur] = nums[cur], nums[i]
                        break
                    cur += 1
                
                
        