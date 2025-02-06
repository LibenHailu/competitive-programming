class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        x = 31
        while n:
            ans |= (n & 1) << x 
            x -= 1
            n >>= 1
        return ans