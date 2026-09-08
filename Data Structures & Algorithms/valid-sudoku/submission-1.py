class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        set_box = {k: set() for k in range(9) }
        set_row = {k: set() for k in range(9) }
     
        for i in range(9):
            set_line = set()

            for j in range(9):

                if board[i][j] == '.':
                    continue

                if board[i][j] in set_line:
                    return False
                else:
                    set_line.add(board[i][j])

                if board[i][j] in set_row[j]:
                    return False
                else:
                    set_row[j].add(board[i][j])

                if board[i][j] in set_box[(j // 3) * 3 + (i // 3)]:
                    return False
                else:
                    set_box[(j // 3) * 3 + (i // 3)].add(board[i][j])

                

               
        return True



