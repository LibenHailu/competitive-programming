class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        memo = [[0] * (n + 1)  for _  in range(m + 1)]
        for r in range(m -1, -1, -1):
            for c in range(n-1, -1, -1):
                if nums1[c] == nums2[r]:
                    memo[r][c] = 1 + memo[r + 1][c + 1]
        return max(max(row) for row in memo)
    