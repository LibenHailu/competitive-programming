class Solution:
    def reverse(self, x: int) -> int:
        target, remaining = 0, abs(x)
        while remaining:
            target = 10 * target + remaining % 10
            if target >  2**31 - 1:
                return 0
            remaining //= 10
        return -target if x < 0 else target
            