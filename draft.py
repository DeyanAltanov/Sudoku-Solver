# Extracting the input into a list.
board = list(open("input.txt").read().split('\n'))

# Converting each element from a string into a list of digits. This is now a matrix, where each element represents the row of the board.
for element in range(len(board)):
    board[element] = board[element].replace("[", "")
    board[element] = board[element].replace("]", "")
    board[element] = list(map(int, board[element].split(",")))

# Creating a dictionary for each row, col and grid of the board.
rows = {}
cols = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
grids = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

for row in range(1, len(board) + 1):
    rows[row] = board[row - 1]
    for i in range(1, 10):
        cols[i].append(board[row - 1][i - 1])

grid_list = []
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        grid_list.append(board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3])

for i in range(1, len(grid_list) + 1):
    grids[i] = grid_list[i - 1]

for key, grid in grids.items():
    grid[:] = (value for value in grid if value != 0)


# Creating a function to identify in which grid the element is part of.


def identify_grid(row, col):
    if 1 <= row <= 3 and 1 <= col <= 3:
        grid = 1
    elif 1 <= row <= 3 and 4 <= col <= 6:
        grid = 2
    elif 1 <= row <= 3 and 7 <= col <= 9:
        grid = 3
    elif 4 <= row <= 6 and 1 <= col <= 3:
        grid = 4
    elif 4 <= row <= 6 and 4 <= col <= 6:
        grid = 5
    elif 4 <= row <= 6 and 7 <= col <= 9:
        grid = 6
    elif 7 <= row <= 9 and 1 <= col <= 3:
        grid = 7
    elif 7 <= row <= 9 and 4 <= col <= 6:
        grid = 8
    elif 7 <= row <= 9 and 7 <= col <= 9:
        grid = 9
    return grid


def remove_value_from_potential_values(potential_values, value):
    for key, values in potential_values.items():
        if value in values:
            values.remove(value)
    return potential_values


def empty_cell_checker(rows):
    for key, values in rows.items():
        if 0 in values:
            return True
    return False


while any(0 in value for value in rows.values()) is True:
    for row in rows:
        potential_values = {}
        for element in range(len(rows[row])):
            value = rows[row][element]
            if value == 0:
                col = element + 1
                grid = identify_grid(row, element + 1)
                potential_values[element] = []
                for i in range(1, 10):
                    if i not in rows[row] and i not in cols[col] and i not in grids[grid]:
                        potential_values[element].append(i)

        for key, values in potential_values.items():
            for number in values:
                current_cell = 0
                cell_value = ''
                lists_containing_digit = []
                for k, numbers in potential_values.items():
                    if number in numbers:
                        lists_containing_digit.append(k)
                if len(lists_containing_digit) > 1:
                    for cell in lists_containing_digit:
                        if len(potential_values[cell]) == 1:
                            cell_value = int(cell)
                else:
                    cell_value = int(key)

                if isinstance(cell_value, int):
                    rows[row][cell_value] = number
                    cols[cell_value + 1][row - 1] = number
                    grids[identify_grid(row, cell_value + 1)].append(number)
                    potential_values = remove_value_from_potential_values(potential_values, number)
                    if rows[row][key] != 0:
                        potential_values[key].clear()
                    break