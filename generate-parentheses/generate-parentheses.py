class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr, open_count, close_count):
            if len(curr) == 2 * n and open_count == close_count:
                ans.append("".join(curr))
                return 
            if len(curr) == 2 * n and open_count != close_count:
                return 
            curr.append("(")
            open_count += 1
            backtrack(curr,open_count, close_count)
            open_count -= 1
            curr.pop()
            if open_count > close_count:
                curr.append(")")
                close_count += 1
                backtrack(curr,open_count, close_count)
                close_count -= 1
                curr.pop()
        backtrack([],0,0)     
        return ans