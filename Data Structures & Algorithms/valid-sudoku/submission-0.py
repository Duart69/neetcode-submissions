class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False]*9 for _ in range(9)]
        column = [[False]*9 for _ in range(9)]
        boxes = [[[False]*9 for _ in range(3)]for _ in range(3)]
        for i in range(0,9):
            for j in range(0,9):
                try:
                    value = int(board[i][j])-1
                    if(row[i][value] or column[j][value] or boxes[int(i/3)][int(j/3)][value]):
                        return False
                    row[i][value] = True
                    column[j][value] = True
                    boxes[int(i/3)][int(j/3)][value] = True
                except ValueError:
                    pass
        return True
