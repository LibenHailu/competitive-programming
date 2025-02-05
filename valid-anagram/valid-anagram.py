class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        
        if len(s_count) != len(t_count):
            return False
        
        if s_count == t_count:
            return True
        
        return False