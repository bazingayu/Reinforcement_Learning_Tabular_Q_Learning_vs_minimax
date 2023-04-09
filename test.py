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
from TQPlayer import TQPlayer
from tic_board import Board
from MinMaxPlayer import MinMaxPlayer
from TQPlayer import TQPlayer
from DummyPlayer import DummyPlayer


def your_turn(Player, board):
    if board.steps >= 9 or board.game_over():
        return

    if board.steps == 0:
        coord = [choice([0, 1, 2]), choice([0, 1, 2])]
    else:
        coord = Player.get_move(board)

    board.set_move(coord, Player.side)




def minmaxvsminmax():
    '''
    run 100 times to statistic win & lose & equal result
    :return:
    '''
    os.system('cls')
    Player1Mark = 'X'
    Player2Mark = 'O'
    Player1Num = 1
    Player2Num = -1
    my_board = Board(Player1Num, Player2Num, Player1Mark, Player2Mark)
    player1 = MinMaxPlayer(Player1Num)
    player2 = MinMaxPlayer(Player2Num)


    iter = 100
    while (iter > 0):
        iter -= 1
        my_board.new_game()
        first = choice(['Y', 'N'])
        print(f"----------------------------Game [{100-iter} starts]-------------------------------")
        while my_board.steps < 9 and not my_board.game_over():
            if first == 'N':
                your_turn(player1, my_board)
                your_turn(player2, my_board)
            else:
                your_turn(player2, my_board)
                your_turn(player1, my_board)
        if my_board.wins(Player1Num):
            my_board.render()
            print('player 1 win')
        elif my_board.wins(Player2Num):
            my_board.render()
            print('Player 2 win')
        else:
            my_board.render()
            print('Draw')
        print(f"---------------------------------Game {100-iter} ends ---------------------------------")

def TQvsminmax():
    '''
    run 100 times to statistic win & lose & equal result
    :return:
    '''
    os.system('cls')
    Player1Mark = 'X'
    Player2Mark = 'O'
    Player1Num = 1
    Player2Num = -1
    my_board = Board(Player1Num, Player2Num, Player1Mark, Player2Mark)
    player1 = MinMaxPlayer(Player1Num)
    player2 = TQPlayer(Player2Num)


    iter = 10000
    while (iter > 0):
        iter -= 1
        my_board.new_game()
        player2.new_game()
        first = choice(['Y', 'N'])
        print(f"----------------------------Game [{10000-iter} starts]-------------------------------")
        while my_board.steps < 9 and not my_board.game_over():
            if first == 'N':
                your_turn(player2, my_board)
                your_turn(player1, my_board)
            else:
                your_turn(player1, my_board)
                your_turn(player2, my_board)
        player2.backtrace(my_board)
        my_board.render()
        if my_board.wins(Player1Num):
            print('MinMax win')
        elif my_board.wins(Player2Num):
            print('TQ-learning win')
        else:
            print('Draw')
        print(f"---------------------------------Game {10000-iter} ends ---------------------------------")

def TQvsDummy():
    '''
    run 100 times to statistic win & lose & equal result
    :return:
    '''
    os.system('cls')
    Player1Mark = 'X'
    Player2Mark = 'O'
    Player1Num = 1
    Player2Num = -1
    my_board = Board(Player1Num, Player2Num, Player1Mark, Player2Mark)
    player1 = DummyPlayer(Player1Num)
    player2 = TQPlayer(Player2Num)


    iter = 10000
    while (iter > 0):
        iter -= 1
        my_board.new_game()
        player2.new_game()
        first = choice(['Y', 'N'])
        print(f"----------------------------Game [{10000-iter} starts]-------------------------------")
        while my_board.steps < 9 and not my_board.game_over():
            if first == 'N':
                your_turn(player2, my_board)
                your_turn(player1, my_board)
            else:
                your_turn(player1, my_board)
                your_turn(player2, my_board)
        player2.backtrace(my_board)
        my_board.render()
        if my_board.wins(Player1Num):
            print('Dummy Player win')
        elif my_board.wins(Player2Num):
            print('TQ-learning win')
        else:
            print('Draw')
        print(f"---------------------------------Game {10000-iter} ends ---------------------------------")

def TQvsTQ():
    '''
    run 100 times to statistic win & lose & equal result
    :return:
    '''
    os.system('cls')
    Player1Mark = 'X'
    Player2Mark = 'O'
    Player1Num = 1
    Player2Num = -1
    my_board = Board(Player1Num, Player2Num, Player1Mark, Player2Mark)
    player1 = TQPlayer(Player1Num)
    player2 = TQPlayer(Player2Num)


    iter = 100000
    while (iter > 0):
        iter -= 1
        my_board.new_game()
        player1.new_game()
        player2.new_game()
        first = choice(['Y', 'N'])
        print(f"----------------------------Game [{10000-iter} starts]-------------------------------")
        while my_board.steps < 9 and not my_board.game_over():
            if first == 'N':
                your_turn(player2, my_board)
                your_turn(player1, my_board)
            else:
                your_turn(player1, my_board)
                your_turn(player2, my_board)
        player2.backtrace(my_board)
        player1.backtrace(my_board)
        my_board.render()
        if my_board.wins(Player1Num):
            print('TQ-learning 1 win')
        elif my_board.wins(Player2Num):
            print('TQ-learning 2 win')
        else:
            print('Draw')
        print(f"---------------------------------Game {10000-iter} ends ---------------------------------")

def choosePlayer(playerName, playerNum):
    if "minmax" in playerName:
        player = MinMaxPlayer(playerNum)
    elif "tq" in playerName:
        player = TQPlayer(playerNum)
    else:
        player = DummyPlayer(playerNum)
    return player

def Player1VsPlayer2(player1Name, player2Name, iter):
    os.system('cls')
    Player1Mark = 'X'
    Player2Mark = 'O'
    Player1Num  =  1
    Player2Num  = -1
    my_board = Board(Player1Num, Player2Num, Player1Mark, Player2Mark)
    player1 = choosePlayer(player1Name, Player1Num)
    player2 = choosePlayer(player2Name, Player2Num)

    while (iter > 0):
        iter -= 1
        my_board.new_game()
        player1.new_game()
        player2.new_game()
        first = choice(['Y', 'N'])
        print(f"-----------------------{player1Name}-vs-{player2Name}--------------------------------")
        print(f"-------------------------Game [{10000 - iter} starts]-------------------------------")
        while my_board.steps < 9 and not my_board.game_over():
            if first == 'N':
                your_turn(player2, my_board)
                your_turn(player1, my_board)
            else:
                your_turn(player1, my_board)
                your_turn(player2, my_board)
        player2.backtrace(my_board)
        player1.backtrace(my_board)
        my_board.render()
        if my_board.wins(Player1Num):
            print(f'{player1Name} win')
        elif my_board.wins(Player2Num):
            print(f'{player2Name} win')
        else:
            print('Draw')
        print(f"---------------------------------Game {10000 - iter} ends ---------------------------------")

if __name__ == '__main__':
    Player1VsPlayer2("minmax", "tq", 100000)
