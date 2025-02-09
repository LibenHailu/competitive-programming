class Solution:
    def mySqrt(self, x: int) -> int:
        best = 0
        left = 1
        right = x 
        while left <= right:
            mid = (right + left) // 2
            if mid ** 2 > x:
                right = mid - 1
            else:
                best = mid
                left = mid + 1
        return best