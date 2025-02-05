class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = []
        for c in s:
            if c.isalnum():
                sanitized.append(c.lower())
        left, right = 0, len(sanitized) - 1
        while left <= right:
            if sanitized[left] != sanitized[right]:
                return False
            left += 1
            right -= 1
        return True
