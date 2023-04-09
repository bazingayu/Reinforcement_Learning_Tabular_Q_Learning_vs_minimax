'''
@author: Junwei Yu
@contact : yuju@tcd.ie
@file: tic_board.py
@time: 2023/3/22 17:45
'''
import numpy as np
class Board():
    '''
    Board Class
    '''
    def __init__(self, Player1, Player2, Player1Mark, Player2Mark):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
        self.steps = 0
        self.Player1 = Player1
        self.Player2 = Player2
        self.Player1Mark = Player1Mark
        self.Player2Mark = Player2Mark
        self.NumOfOptions = 9
        self.ALL_STEPS = 9
        self.ROW_COUNT = 3
        self.COLUME_COUNT = 3

    def new_game(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
        self.steps = 0

    def wins(self, player):
        '''
        :param state: the board
        :param player: human or computer
        :return: true if the player wins
        '''
        board = self.board
        win_state = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False

    def game_over(self):
        return self.wins(self.Player1) or self.wins(self.Player2)

    def set_move(self, coord, player):
        if self.valid_move(coord):
            self.board[coord[0]][coord[1]] = player
            self.steps += 1
            return True
        else:
            return False

    def valid_move(self, coord):
        if self.board[coord[0]][coord[1]] == 0:
            return True
        else:
            return False

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
        for row in self.board:
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)