'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
1. A Sudoku board (partially filled) could be valid but is not necessarily solvable.
2. Only the filled cells need to be validated according to the mentioned rules.
Example 1: Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]] Output: true
Example 2: Input: board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]] Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Answer:
1. Create a set to store the numbers in each row
2. Create a set to store the numbers in each column
3. Create a set to store the numbers in each 3x3 sub-box
4. Iterate through each element in the board
5. If the element is not a '.', check if the element is in the row, column, or sub-box
6. If the element is in the row, column, or sub-box, return False
7. If the element is not in the row, column, or sub-box, add the element to the row, column, and sub-box
8. Return True
Hint: Use the floor division operator to find the row and column of each element in the board
'''

def isValidSudoku(board):
    for i in range(9):
        row = set()
        col = set()
        box = set()
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
            if board[j][i] != '.':
                if board[j][i] in col:
                    return False
                col.add(board[j][i])
            if board[i//3*3+j//3][i%3*3+j%3] != '.':
                if board[i//3*3+j//3][i%3*3+j%3] in box:
                    return False
                box.add(board[i//3*3+j//3][i%3*3+j%3])
    return True

def isValidSudokuOptimized(board):
    seen = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                if (i, board[i][j]) in seen or (board[i][j], j) in seen or (i//3, j//3, board[i][j]) in seen:
                    return False
                seen.add((i, board[i][j]))
                seen.add((board[i][j], j))
                seen.add((i//3, j//3, board[i][j]))
    return True
