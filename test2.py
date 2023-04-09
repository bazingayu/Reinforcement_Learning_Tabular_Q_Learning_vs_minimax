'''
@author: Junwei Yu
@contact : yuju@tcd.ie
@file: TabularQlearning.py
@time: 2023/3/22 13:27
'''
import os
import time
from random import choice
from math import inf
import numpy as np
from tqdm import tqdm
from TQPlayer import TQPlayer
import tic_board
import connect4_board
from MinMaxPlayer import MinMaxPlayer
from TQPlayer import TQPlayer
from DummyPlayer import DummyPlayer
from HumanPlayer import HumanPlayer
from matplotlib import pyplot as plt


def your_turn(Player, board):
    if board.steps >= board.ALL_STEPS or board.game_over():
        return
    if board.ALL_STEPS != 9:
        if board.steps == 0:
            col = choice(list(range(board.COLUME_COUNT)))
        else:
            [col, _] = Player.get_move(board)
        board.set_move(col, Player.side)

    else:
        if board.steps == 0:
            coord = [choice([0, 1, 2]), choice([0, 1, 2])]
        else:
            coord = Player.get_move(board)

        board.set_move(coord, Player.side)

def choosePlayer(playerName, playerNum, alpha=0.5):
    if "minimax" in playerName:
        player = MinMaxPlayer(playerNum)
    elif "tq" in playerName:
        player = TQPlayer(playerNum)
    elif "human" in playerName:
        player = HumanPlayer(playerNum)
    else:
        player = DummyPlayer(playerNum)
    return player

def Player1VsPlayer2(player1Name, player2Name, num_battles, games_per_battle):
    os.system('cls')
    Player1Mark = 'X'
    Player2Mark = 'O'
    Player1Num  =  1
    Player2Num  = -1
    my_board = Board(Player1Num, Player2Num, Player1Mark, Player2Mark)
    player1 = choosePlayer(player1Name, Player1Num)
    player2 = choosePlayer(player2Name, Player2Num)
    print(f"-----------------------{player1Name}-vs-{player2Name}--------------------------------")
    p1_wins = []
    p2_wins = []
    draws = []
    count = []
    for i in tqdm(range(num_battles)):
        p1 = 0
        p2 = 0
        draw = 0
        for j in range(games_per_battle):
            my_board.new_game()
            player1.new_game()
            player2.new_game()
            first = choice(['Y', 'N'])
            while my_board.steps < my_board.ALL_STEPS and not my_board.game_over():
                if first == 'N':
                    print(player2)
                    your_turn(player2, my_board)
                    your_turn(player1, my_board)
                else:
                    your_turn(player1, my_board)
                    your_turn(player2, my_board)
            player2.backtrace(my_board)
            player1.backtrace(my_board)
            # my_board.render()
            if my_board.wins(Player1Num):
                if 'human' in player1Name or 'human' in player2Name:
                    my_board.render()
                    print(f'{player1Name} wins')
                p1 += 1
            elif my_board.wins(Player2Num):
                if 'human' in player1Name or 'human' in player2Name:
                    my_board.render()
                    print(f'{player2Name} wins')
                p2 += 1
            else:
                if 'human' in player1Name or 'human' in player2Name:
                    my_board.render()
                    print(f'Draw')
                draw += 1
        p1_wins.append(p1)
        p1_wins.append(p1)
        p2_wins.append(p2)
        p2_wins.append(p2)
        draws.append(draw)
        draws.append(draw)
        count.append(i*games_per_battle)
        count.append((i+1)*games_per_battle)
        # print(f"This is the {i} round battle, p1 = {p1}, p2 = {p2}, draws = {draw}")

    plt.ylabel('Game outcomes in %')
    plt.xlabel('Game number')

    plt.plot(count, draws, 'r-', label='Draw')
    plt.plot(count, p1_wins, 'g-', label=f'{player1Name} wins')
    plt.plot(count, p2_wins, 'b-', label=f'{player2Name} wins')
    plt.legend(loc="best", shadow=True, fancybox=True, framealpha=0.7)
    plt.show()


if __name__ == '__main__':
    # Board = tic_board.Board
    Board = connect4_board.Board
    Player1VsPlayer2("tq1-tabular-Q-learning", "tq2-tabular-Q-learning", 1000, 100)
