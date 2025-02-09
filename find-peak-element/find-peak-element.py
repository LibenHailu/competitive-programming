class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        eg: [1,2,1,3,5,6,4]
            left, right = 0, len(nums) - 1
            
            mid = 3
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
            
        