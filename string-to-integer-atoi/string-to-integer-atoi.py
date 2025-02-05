class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == "-" else 1
        res = 0
        for i in range(len(s)):
            if i == 0 and (s[i] == "-" or s[i] == "+"):
                continue
            elif res == 0 and s[i] == "0":
                continue
            elif not s[i].isnumeric():
                break
            elif s[i].isnumeric():
                res = res * 10 + int(s[i])
        if res * sign > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res * sign < -2 ** 31:
            return -2 ** 31
        return res *  sign
                
        