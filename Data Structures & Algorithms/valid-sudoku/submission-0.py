class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        set_box = {k: set() for k in range(9) }
        set_row = {}
        for i in range(9):
            set_line = set()
            set_row[i] = set()
            for j in range(9):

                if board[i][j] == '.':
                    continue

                if board[i][j] in set_line:
                    return False
                else:
                    set_line.add(board[i][j])

                if board[i][j] in set_row[i]:
                    return False
                else:
                    set_row[i].add(board[i][j])

                if board[i][j] in set_box[(j // 3) * 3 + (i // 3)]:
                    return False
                else:
                    set_box[(j // 3) * 3 + (i // 3)].add(board[i][j])

                

               
        return True



