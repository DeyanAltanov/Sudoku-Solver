def gridder(board):
    grids = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    grid_list = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            grid_list.append(board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3])

    for i in range(0, len(grid_list)):
        grids[i] = grid_list[i]
    return grids


def identify_grid(row, col):
    if 0 <= row <= 2 and 0 <= col <= 2:
        grid = 0
    elif 0 <= row <= 2 and 3 <= col <= 5:
        grid = 1
    elif 0 <= row <= 2 and 6 <= col <= 8:
        grid = 2
    elif 3 <= row <= 5 and 0 <= col <= 2:
        grid = 3
    elif 3 <= row <= 5 and 3 <= col <= 5:
        grid = 4
    elif 3 <= row <= 5 and 6 <= col <= 8:
        grid = 5
    elif 6 <= row <= 8 and 0 <= col <= 2:
        grid = 6
    elif 6 <= row <= 8 and 3 <= col <= 5:
        grid = 7
    elif 6 <= row <= 8 and 6 <= col <= 8:
        grid = 8
    return grid


def find_empty_cell(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col
    return None


def validate_value(board, number, cell, grids):
    row = cell[0]
    col = cell[1]
    for i in range(len(board[0])):
        if board[row][i] == number and col != i:
            return False

    for i in range(len(board)):
        if board[i][col] == number and row != i:
            return False

    grid = identify_grid(row, col)
    if number in grids[grid]:
        return False
    return True


def board_solver(board):
    find = find_empty_cell(board)
    if not find:
        return True
    else:
        row, col = find
        grids = gridder(board)

    for i in range(1, 10):
        if validate_value(board, i, (row, col), grids):
            board[row][col] = i
            if board_solver(board):
                return True
            board[row][col] = 0
    return False