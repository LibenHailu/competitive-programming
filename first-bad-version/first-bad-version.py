# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n 
        # best = -1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if isBadVersion(mid):
        #         best = mid
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return best
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right