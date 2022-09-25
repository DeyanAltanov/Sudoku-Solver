from board import Board
from functions import board_solver

board = Board().get_board()

if board_solver(board):
    solution = '[\n'
    for row in board:
        solution += f" {row},\n"
    solution += ']'
    file = open('output.txt', 'w')
    file.write(solution)
    file.close()