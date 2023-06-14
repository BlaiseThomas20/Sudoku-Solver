# sudokuSolver.py


def solver(board):
    """ Solves the common sudoku game 
    by using backtracking and returning a solution"""
    
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True
    
    for i in range(1, 10):
        if validate(board, (row, col), i):
            board[row][col] = i

        if solve(board):
            return True
        
        board[row][col] = 0
        
    return False

def validate(board, position, number):
    """_summary_

    Args:
        board (_type_): 2D LIST OF INTS
        position (_type_): ROWS AND COLUMNS
        number (_type_): INT
        return: bool
    """
    
    #Row
    for i in range(0)