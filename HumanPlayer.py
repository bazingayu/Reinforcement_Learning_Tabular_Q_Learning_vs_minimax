'''
@author: Junwei Yu
@contact : yuju@tcd.ie
@file: HumanPlayer.py
@time: 2023/3/29 17:29
'''

from random import choice
class HumanPlayer():
    '''
    A Tic Tac Toe Player, implement Tabular Q Learning
    '''
    def __init__(self, side, alpha=0.9, gamma=0.95, q_init=0.6):
        self.side = side

    def get_move(self, board):
        board.render()
        if board.ALL_STEPS == 9:
            i = int(input("Please Input Your step 1~9"))
            i -= 1
            x = i // 3
            y = i % 3
            return [x, y]
        else:
            m = int(input("Please Input Your Column 1~8"))
            return [m - 1, None]

    def new_game(self):
        return
    def backtrace(self, board):
        return