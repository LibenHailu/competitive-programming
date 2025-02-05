class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = 200
        for word in strs:
            minLength = min(minLength, len(word)) 
        ans = ""
        for i in range(minLength):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    return ans 
            ans += c
        return ans
        