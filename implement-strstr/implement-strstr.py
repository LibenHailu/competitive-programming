class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack) -len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        