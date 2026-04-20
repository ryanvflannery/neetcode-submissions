# The input is a Sudoku board
# We want to make we have a Valid Sudoku board
# The ouput will be true if valid board false if not valid

# Each row must contain digits 1 - 9 no duplicates
# Each column must contain the digits 1 - 9 no duplictaes

# 3x3 doesnt need to be filled in just no duplicates

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        columns = defaultdict(set)

        squares = defaultdict(set) # Key = (r/3, c/3)


        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # Have we found a duplicate
                if (board[r][c] in rows[r] or
                   board[r][c] in columns[c] or 
                   board[r][c] in squares[(r // 3, c // 3)]):
                   return False
                
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])

        return True


        # Check each row for duplicates 

        # Check each column for duplicates 

        # Check each 3x3 sub box no duplicates