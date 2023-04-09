'''
@author: Junwei Yu
@contact : yuju@tcd.ie
@file: TQPlayer.py
@time: 2023/3/22 14:08
'''
import numpy as np
import json


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class TQPlayer():
    '''
    A Tic Tac Toe Player, implement Tabular Q Learning
    '''
    def __init__(self, side, alpha=0.5, gamma=0.95, q_init=0.6):
        # alpha too big, care about the latter, too small, care about the previous
        self.side = side
        self.q = {}
        self.move_history = []
        self.learning_rate = alpha
        self.value_discount = gamma
        self.q_init_val = q_init

    def hash_value(self, board):
        # hash_for_game_tic
        res = 0
        for x in range(len(board.board)):
            for y in range(len(board.board[0])):
                res *= 3
                value = board.board[x][y]
                if value == self.side:
                    res += 1
                elif value == -self.side:
                    res += 2
                else:
                    res += 0
        return res

    def get_q(self, board_hash, board):
        if board_hash in self.q:
            qvals = self.q[board_hash]
        else:
            qvals = np.full(board.NumOfOptions, self.q_init_val)
            self.q[board_hash] = qvals
        return qvals

    def get_move(self, board):
        board_hash = self.hash_value(board)
        qvals = self.get_q(board_hash, board)
        if board.ALL_STEPS == 9:
            while True:
                m = np.argmax(qvals) # 0-8
                # m is the index of the move
                # get the x and y in the value
                x = m // 3
                y = m % 3
                if board.board[x][y] != 0:
                    qvals[m] = -10.0
                else:
                    # the location is ok
                    self.move_history.append((board_hash, m))
                    return [x, y]
        else:
            # CONNECT 4 GAME
            while True:
                m = np.argmax(qvals)
                if board.valid_move(m):
                    self.move_history.append((board_hash, m))
                    return [m, None]
                else:
                    qvals[m] = -10.0



    def backtrace(self, board):
        if board.wins(self.side):
            final_value = 1.0
        elif board.wins(-self.side):
            final_value = 0.0
        else:
            final_value = 0.5

        self.move_history.reverse()
        next_max = -1.0
        for h in self.move_history:
            qvals = self.get_q(h[0], board)
            if next_max < 0: #Fisrt time through the loop
                qvals[h[1]] = final_value
            else:
                qvals[h[1]] = qvals[h[1]] * (1.0-self.learning_rate) + self.learning_rate * self.value_discount * next_max

            next_max = max(qvals)

        # info_json = json.dumps(self.q, sort_keys=False, indent=4, separators=(',', ': '), cls=NpEncoder)
        #
        # f = open('tq_model.json', 'w')
        # f.write(info_json)


    def new_game(self):
        self.move_history = []