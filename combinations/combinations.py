class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(first_num, curr):
            if len(curr) == k:
                res.append(curr[:])
                return 
            
            for num in range(first_num, n + 1):
                curr.append(num)
                backtrack(num + 1, curr)
                curr.pop()
        backtrack(1, [])
        return res
        