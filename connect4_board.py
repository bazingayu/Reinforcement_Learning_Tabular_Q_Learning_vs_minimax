'''
@author: Junwei Yu
@contact : yuju@tcd.ie
@file: connect4_board.py
@time: 2023/3/27 14:39
'''
import os
import numpy as np
class Board():
    '''
    Board Class
    '''
    def __init__(self, Player1, Player2, Player1Mark, Player2Mark):
        self.ROW_COUNT = 5
        self.COLUME_COUNT = 6
        self.board = np.zeros((self.ROW_COUNT, self.COLUME_COUNT))

        self.steps = 0
        self.Player1 = Player1
        self.Player2 = Player2
        self.Player1Mark = Player1Mark
        self.Player2Mark = Player2Mark
        self.NumOfOptions = self.COLUME_COUNT
        self.ALL_STEPS = self.ROW_COUNT * self.COLUME_COUNT

    def create_win_paths(self):
        self.win_paths = []
        # horizontal
        for c in range(self.COLUME_COUNT - 3):
            for r in range(self.ROW_COUNT):
                self.win_paths.append([self.board[r][c], self.board[r][c+1], self.board[r][c+2], self.board[r][c+3]])

        # Check vertical locations for win
        for c in range(self.COLUME_COUNT):
            for r in range(self.ROW_COUNT - 3):
                self.win_paths.append([self.board[r][c], self.board[r+1][c], self.board[r+2][c], self.board[r+3][c]])

        # Check positively sloped diaganols
        for c in range(self.COLUME_COUNT - 3):
            for r in range(self.ROW_COUNT - 3):
                self.win_paths.append([self.board[r][c], self.board[r + 1][c + 1], self.board[r + 2][c + 2], self.board[r + 3][c + 3]])

            # Check negatively sloped diaganols
        for c in range(self.COLUME_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                self.win_paths.append(
                    [self.board[r][c], self.board[r - 1][c + 1], self.board[r - 2][c + 2], self.board[r - 3][c + 3]])

    def new_game(self):
        self.board = np.zeros((self.ROW_COUNT, self.COLUME_COUNT))
        self.steps = 0

    def wins(self, player):
        '''
        :param state: the board
        :param player: human or computer
        :return: true if the player wins
        '''
        self.create_win_paths()
        if [player, player, player, player] in self.win_paths:
            return True
        else:
            return False

    def game_over(self):
        return self.wins(self.Player1) or self.wins(self.Player2)

    def get_next_open_row(self, col):
        for r in range(self.ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def set_move(self, col, player):
        if self.valid_move(col):
            r = self.get_next_open_row(col)
            self.board[r][col] = player
            self.steps += 1
            return True
        else:
            return False

    def valid_move(self, col):
        return self.board[self.ROW_COUNT-1][col] == 0

    def render(self):
        '''
        print the information of the borad
        :param state: board
        :param c_choice:
        :param h_choice:
        :return:
        '''
        chars = {self.Player1: self.Player1Mark, self.Player2: self.Player2Mark, 0: ''}
        str_line = '---------------------'
        print('\n' + str_line)
        help = np.flip(np.array(self.board).copy(), 0)
        for row in help:
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)
