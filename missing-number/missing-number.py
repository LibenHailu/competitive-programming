class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in nums:
            # print(nums)
            if num == -1:
                continue
            cur = num 
            while cur != - 1:
                if cur < len(nums):
                    temp = nums[cur]
                    nums[cur] = -1
                    cur = temp
                else:
                    cur = -1
        
        for i in range(len(nums)):
            if nums[i] != -1:
                return i
        return i + 1