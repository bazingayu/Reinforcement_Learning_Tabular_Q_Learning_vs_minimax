'''
@author: Junwei Yu
@contact : yuju@tcd.ie
@file: DummyPlayer.py
@time: 2023/3/22 22:28
'''
from random import choice
class DummyPlayer():
    '''
    A Tic Tac Toe Player, implement Tabular Q Learning
    '''
    def __init__(self, side, alpha=0.9, gamma=0.95, q_init=0.6):
        self.side = side

    def get_move(self, board):
        if board.ALL_STEPS == 9:
            valid_moves = []
            for x in range(3):
                for y in range(3):
                    if (board.board[x][y] != 0):  # already occupied
                        continue
                    board.board[x][y] = self.side
                    if board.wins(self.side):  # if exist a winning move, select it
                        board.board[x][y] = 0
                        return [x, y]
                    board.board[x][y] = -self.side  # prevent computer winning
                    if board.wins(-self.side):
                        board.board[x][y] = 0
                        return [x, y]
                    board.board[x][y] = 0
                    valid_moves.append([x, y])
        else:
            valid_moves = []
            for m in range(board.COLUME_COUNT):
                if board.valid_move(m) == False:
                    continue
                r = board.get_next_open_row(m)
                board.board[r][m] = self.side
                if board.wins(self.side):
                    board.board[r][m] = 0
                    return [m, None]
                board.board[r][m] = -self.side
                if board.wins(-self.side):
                    board.board[r][m] = 0
                    return[m, None]
                board.board[r][m] = 0
                valid_moves.append([m, None])
        return choice(valid_moves)

    def new_game(self):
        return
    def backtrace(self, board):
        return