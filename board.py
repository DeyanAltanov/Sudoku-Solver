class Board:
    def __init__(self):
        self.board = list(open("input.txt").read().split('\n'))

    def get_board(self):
        for element in range(len(self.board)):
            self.board[element] = self.board[element].replace("[", "")
            self.board[element] = self.board[element].replace("]", "")
            self.board[element] = list(map(int, self.board[element].split(",")))
        return self.board