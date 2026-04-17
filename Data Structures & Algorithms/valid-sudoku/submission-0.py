class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dict={}
        row_dict={}
        mat_dict={}

        for i in range(len(board)):
            col_dict={}
            row_dict={}
            for j in range(len(board[0])):
                if board[i][j] !="." and board[i][j]in row_dict:
                    return False
                row_dict[board[i][j]] = row_dict.get(board[i][j], 0) +1
                if  board[j][i] !="." and board[j][i]in col_dict:
                    return False
                col_dict[board[j][i]] = col_dict.get(board[j][i], 0) +1

                if  board[i][j] !="." and board[i][j] in mat_dict.get((i//3,j//3),{}):
                    return False
                mat_dict[(i//3,j//3)] =  mat_dict.get((i//3,j//3),set())
                mat_dict[(i//3,j//3)].add(board[i][j])

        return True

