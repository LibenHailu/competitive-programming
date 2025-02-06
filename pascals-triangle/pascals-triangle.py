class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for row in range(1 , numRows + 1):
            if row == 1:
                ans.append([1])
                continue
            if row == 2:
                ans.append([1, 1])
                continue
            cur = []
            cur.append(1)
            for i in range(1, row - 1):
                cur.append(ans[row - 2][i - 1] + ans[row - 2][i])
            cur.append(1)
            ans.append(cur)
        return ans
            
            