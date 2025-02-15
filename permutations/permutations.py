class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(visited):
            if len(visited) == len(nums):
                ans.append(visited[:])
            
            for num in nums:
                if num not in visited:
                    visited.append(num)
                    backtrack(visited)
                    visited.pop()
        backtrack([])
        return ans