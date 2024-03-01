import collections
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = collections.defaultdict(set) #(row_num) -> set containing what numbers in row
        col_dict = collections.defaultdict(set) #(col_num) -> set containing what numbers in col 
        square_dict = collections.defaultdict(set) #(row//3, col//3) index
        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] == ".":
                    continue
                else:
                    if (board[row_idx][col_idx] in row_dict[row_idx] or board[row_idx][col_idx] in col_dict[col_idx]
                    or board[row_idx][col_idx] in square_dict[(row_idx//3, col_idx//3)]):
                        return False
                    else:
                        row_dict[row_idx].add(board[row_idx][col_idx])
                        col_dict[col_idx].add(board[row_idx][col_idx])
                        square_dict[(row_idx//3,col_idx//3)].add(board[row_idx][col_idx])
        return True
