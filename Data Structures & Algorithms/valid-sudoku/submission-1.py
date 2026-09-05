class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                try:
                    value = int(board[i][j])
                    if(("column", j, value) in seen or ("row", i, value) in seen or ("box", int(i/3),int(j/3), value) in seen):
                        return False
                    seen.add(("column", j, value))
                    seen.add(("row", i, value))
                    seen.add(("box", int(i/3),int(j/3), value))
                except ValueError:
                    pass
        return True