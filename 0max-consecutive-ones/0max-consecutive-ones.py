class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # ans  = [0]
        # for num in nums:
        #     if num == 1:
        #         ans.append(ans[-1] + 1)
        #     else:
        #         ans.append(0)
        # return max(ans)
        maxOnes = 0 
        res = 0
        for num in nums:
            if num == 1:
                maxOnes += 1
            else:
                maxOnes = 0
            res = max(maxOnes, res)
        return res