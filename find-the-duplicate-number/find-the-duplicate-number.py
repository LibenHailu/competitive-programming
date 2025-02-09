class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        eg: [1,3,4,2,2]
        
        
        '''
        if len(nums) == 2:
            return nums[0]
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        