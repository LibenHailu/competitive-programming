class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        stack = []
        for c in s:
            if c in close and stack and close[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
                