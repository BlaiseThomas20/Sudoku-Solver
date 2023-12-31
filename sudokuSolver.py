def main():
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 0, 0, 0, 7]
    ]

    solver(board)
    print_board(board)

def solver(board):
    find = find_empty_position(board)
    if find is None:
        return True
    
    row, col = find
    
    for i in range(1, 10):
        if validate(board, (row, col), i):
            board[row][col] = i

            if solver(board):
                return True

            board[row][col] = 0

    return False

def validate(board, position, number):
    for i in range(0, len(board)):
        if board[position[0]][i] == number and position[1] != i:
            return False

    for i in range(0, len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True

def find_empty_position(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")
                

if __name__ == "__main__":
    main()