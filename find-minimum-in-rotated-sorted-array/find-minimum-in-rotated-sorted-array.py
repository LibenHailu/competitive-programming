class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        eg: [3,4,5,1,2]
        
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right] and nums[left] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
                
        