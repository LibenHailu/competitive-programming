class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(i):
            print(i, s[i: i +1], s[i : i + 2])
            if i == len(s):
                return 1
            ans = 0
            if 0 < int(s[i: i +1]) < 10:
                ans += dp(i + 1)
            if i + 2 <= len(s) and 10 <= int(s[i: i +2]) < 27:
                ans += dp(i + 2)
            return ans
        return dp(0)
            