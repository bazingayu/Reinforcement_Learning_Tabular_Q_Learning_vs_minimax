'''
@author: Junwei Yu
@contact : yuju@tcd.ie
@file: MinMaxPlayer.py
@time: 2023/3/22 17:37
'''
import time
from math import inf


class MinMaxPlayer():
    '''
    A Tic Tac Toe Player, implement MinMax Algorithm
    '''
    def __init__(self, side):
        self.side = side # +1 or -1
        self.step = 0
        self.start_time = time.time()


    def evaluate(self, Board):
        if Board.wins(self.side):
            score = +1
        elif Board.wins(-self.side):
            score = -1
        else:
            score = 0
        return score

    def get_move(self, board):
        if board.ALL_STEPS == 9:
            return self.minmax(board, 9-board.steps, self.side, -inf, inf)
        else:
            return self.minmax(board, 5, self.side, -inf, inf)

    def minmax(self, Board, depth, player, alpha, beta):
        '''
        AI function to choose the best move
        :param state: board
        :param depth:  node index in the tree
        :param player: a human or a computer
        :return: a list with [the best row, the best col, the best score]
        '''
        if Board.ALL_STEPS == 9:
            if player == self.side:
                best = [-1, -1, -inf]
            else:
                best = [-1, -1, +inf]

            if depth == 0 or Board.game_over():
                score = self.evaluate(Board)
                return [-1, -1, score]

            for x in range(Board.ROW_COUNT):
                for y in range(Board.COLUME_COUNT):
                    if (Board.board[x][y] != 0):
                        continue
                    Board.board[x][y] = player

                    score = self.minmax(Board, depth - 1, -player, alpha, beta)
                    Board.board[x][y] = 0
                    score[0], score[1] = x, y

                    if player == self.side:
                        if score[2] > best[2]:
                            best = score  # max value
                        alpha = max(alpha, best[2])
                    else:
                        if score[2] < best[2]:
                            best = score  # min value
                        beta = min(beta, best[2])
                    if alpha >= beta:
                        break

            return best
        else:
            if player == self.side:
                best = [-1, -inf]
            else:
                best = [-1, +inf]

            if depth == 0 or Board.game_over():
                score = self.evaluate(Board)
                return [-1, score]

            for m in range(Board.COLUME_COUNT):
                if (Board.board[Board.ROW_COUNT-1][m] != 0):
                    continue
                r = Board.get_next_open_row(m)
                Board.board[r][m] = player
                self.step += 1
                score = self.minmax(Board, depth - 1, -player, alpha, beta)
                Board.board[r][m] = 0
                score[0] = m

                if player == self.side:
                    if score[1] > best[1]:
                        best = score  # max value
                    alpha = max(alpha, best[1])
                else:
                    if score[1] < best[1]:
                        best = score  # min value
                    beta = min(beta, best[1])
                if alpha >= beta:
                    break

            return best

    def new_game(self):
        return
    def backtrace(self, board):
        return

