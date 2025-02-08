class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_height = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != new_height[i]:
                ans += 1
        return ans
        