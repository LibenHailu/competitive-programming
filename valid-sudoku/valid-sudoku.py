class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rmap = defaultdict(list)
        cmap = defaultdict(list)
        square = defaultdict(list)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rmap[r] or board[r][c] in cmap[c] or board[r][c] in square[(r//3,c//3)]:
                    return False
                rmap[r].append(board[r][c])
                cmap[c].append(board[r][c])
                square[(r//3, c//3)].append(board[r][c])
        return True