'''
copied from https://github.com/CodecoolGlobal/tic-tac-toe-python-8-10-24
'''

import os
import random
import time


def init_board():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board


def get_move(board, player):
    row = 3
    col = 3
    valid_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    move = input('Make your move: ')
    if move.lower() == 'quit':
        quit()
    elif move.lower() not in valid_moves:
        print('Not a valid move!')
        return get_move(board, player)
    if 'a' in move.lower():
        row = 0
    elif 'b' in move.lower():
        row = 1
    elif 'c' in move.lower():
        row = 2
    if '1' in move:
        col = 0
    elif '2' in move:
        col = 1
    elif '3' in move:
        col = 2
    if board[row][col] != 0:
        print('Place already taken')
        return get_move(board, player)
    return (row, col)


def get_ai_move(board, player):
    '''
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while board[row][col] != 0:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    return (row, col)
    '''
    corners = [board[0][0], board[0][2], board[2][0], board[2][2]]
    winning_cases = [[board[0][0], board[0][1], board[0][2]], [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]]]
    winning_cases2 = [[board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]],
                      [board[0][2], board[1][2], board[2][2]]]
    winning_cases3 = [board[0][0], board[1][1], board[2][2]]
    winning_cases4 = [board[0][2], board[1][1], board[2][0]]
    for i in winning_cases:
        if sum(i) == 4 and 0 in i:
            row = board.index(i)
            col = i.index(0)
            return(row, col)
    for i in winning_cases2:
        if sum(i) == 4 and 0 in i:
            col = winning_cases2.index(i)
            row = i.index(0)
            return(row, col)
    if sum(winning_cases3) == 4 and 0 in winning_cases3:
        row = winning_cases3.index(0)
        col = winning_cases3.index(0)
        return(row, col)
    if sum(winning_cases4) == 4 and 0 in winning_cases4:
        if winning_cases4.index(0) == 1:
            row, col = 1, 1
            return (row, col)
        elif winning_cases4.index(0) == 0:
            row, col = 0, 2
            return(row, col)
        elif winning_cases4.index(0) == 2:
            row, col = 2, 0
            return(row, col)
    for i in winning_cases:
        if sum(i) == 2 and 1 in i:
            row = board.index(i)
            col = i.index(0)
            return(row, col)
    for i in winning_cases2:
        if sum(i) == 2 and 1 in i:
            col = winning_cases2.index(i)
            row = i.index(0)
            return(row, col)
    if sum(winning_cases3) == 2 and 1 in winning_cases3:
        row = winning_cases3.index(0)
        col = winning_cases3.index(0)
        return(row, col)
    if sum(winning_cases4) == 2 and 1 in winning_cases4:
        if winning_cases4.index(0) == 1:
            row, col = 1, 1
            return (row, col)
        elif winning_cases4.index(0) == 0:
            row, col = 0, 2
            return(row, col)
        elif winning_cases4.index(0) == 2:
            row, col = 2, 0
            return(row, col)
    if board[1][1] == 0:
        row, col = 1, 1
        return(row, col)
    if 0 in corners:
        row = random.randrange(0, 3, 2)
        col = random.randrange(0, 3, 2)
        while board[row][col] != 0:
            row = random.randrange(0, 3, 2)
            col = random.randrange(0, 3, 2)
        return(row, col)
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while board[row][col] != 0:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    return (row, col)


def mark(board, player, row, col):
    try:
        if board[row][col] == 0:
            board[row][col] = player
    except IndexError:
        return


def has_won(board, player):
    if (board[0][0] == board[0][1] == board[0][2] == player or board[1][0] == board[1][1] == board[1][2] == player or
        board[2][0] == board[2][1] == board[2][2] == player or board[0][0] == board[1][0] == board[2][0] == player or
        board[0][1] == board[1][1] == board[2][1] == player or board[0][2] == board[1][2] == board[2][2] == player or
            board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False


def is_full(board):
    if 0 in board[0]:
        return False
    elif 0 in board[1]:
        return False
    elif 0 in board[2]:
        return False
    else:
        return True


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    newboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(len(board)):
        for i in range(len(board[0])):
            if board[x][i] == 0:
                newboard[x][i] = '.'
            if board[x][i] == 1:
                newboard[x][i] = 'X'
            if board[x][i] == 2:
                newboard[x][i] = 'O'
    print('''
               1   2   3
            A  {} | {} | {}
              ---+---+---
            B  {} | {} | {}
              ---+---+---
            C  {} | {} | {}
        '''.format(newboard[0][0], newboard[0][1], newboard[0][2], newboard[1][0], newboard[1][1], newboard[1][2],
                   newboard[2][0], newboard[2][1], newboard[2][2]))


def print_result(winner):
    if winner == 0:
        print("It's a tie! \n")
    if winner == 1:
        print('X won! \n')
    if winner == 2:
        print('O won! \n')


def tictactoe_game(mode='HUMAN-HUMAN'):
    if mode == 'HUMAN-HUMAN':
        board = init_board()
        while not has_won(board, 1) and not has_won(board, 2) and not is_full(board):
            os.system('cls')
            print_board(board)
            row, col = get_move(board, 1)
            mark(board, 1, row, col)
            os.system('cls')
            print_board(board)
            if not has_won(board, 1) and not is_full(board):
                row, col = get_move(board, 2)
                mark(board, 2, row, col)
                print_board(board)

        if has_won(board, 1):
            winner = 1
        elif has_won(board, 2):
            winner = 2
        else:
            winner = 0
        print_result(winner)
        after_menu()
    elif mode == 'HUMAN-AI':
        board = init_board()
        while not has_won(board, 1) and not has_won(board, 2) and not is_full(board):
            os.system('cls')
            print_board(board)
            row, col = get_move(board, 1)
            mark(board, 1, row, col)
            os.system('cls')
            print_board(board)
            if not has_won(board, 1) and not is_full(board):
                row, col = get_ai_move(board, 2)
                mark(board, 2, row, col)
                os.system('cls')
                print_board(board)

        if has_won(board, 1):
            winner = 1
        elif has_won(board, 2):
            winner = 2
        else:
            winner = 0
        print_result(winner)
        after_menu()
    elif mode == 'AI-HUMAN':
        board = init_board()
        while not has_won(board, 1) and not has_won(board, 2) and not is_full(board):
            row, col = get_ai_move(board, 2)
            mark(board, 1, row, col)
            os.system('cls')
            print_board(board)
            if not has_won(board, 1) and not is_full(board):
                row, col = get_move(board, 1)
                mark(board, 2, row, col)
                os.system('cls')
                print_board(board)
        if has_won(board, 1):
            winner = 1
        elif has_won(board, 2):
            winner = 2
        else:
            winner = 0
        print_result(winner)
        after_menu()

    elif mode == 'AI-AI':
        board = init_board()
        while not has_won(board, 1) and not has_won(board, 2) and not is_full(board):
            row, col = get_ai_move(board, 2)
            mark(board, 1, row, col)
            os.system('cls')
            print_board(board)
            time.sleep(2)
            if not has_won(board, 1) and not is_full(board):
                row, col = get_ai_move(board, 2)
                mark(board, 2, row, col)
                os.system('cls')
                print_board(board)
                time.sleep(2)
        if has_won(board, 1):
            winner = 1
        elif has_won(board, 2):
            winner = 2
        else:
            winner = 0
        print_result(winner)
        after_menu()


def after_menu():
    print('1.Play again')
    print('2.Menu')
    print('3.Quit')
    action = input('Play again?')
    while action != '1' or action != '2' or action != '3':
        if action == '1':
            tictactoe_game('AI-AI')
        elif action == '2':
            main_menu()
        elif action == '3':
            quit()
        else:
            action = input('Play again?')


def main_menu():
    os.system('cls')
    print('''
      ________________   _________   ______   __________  ______
     /_  __/  _/ ____/  /_  __/   | / ____/  /_  __/ __ \/ ____/
      / /  / // /  ______/ / / /| |/ /  ______/ / / / / / __/
     / / _/ // /__/_____/ / / ___ / /__/_____/ / / /_/ / /___
    /_/ /___/\____/    /_/ /_/  |_\____/    /_/  \____/_____/
        ''')
    print('1.HUMAN-HUMAN')
    print('2.HUMAN-AI')
    print('3.AI-HUMAN')
    print('4.AI-AI')
    select = input('Choose game mode!')
    if select == 'quit':
        quit()
    elif select == str(1):
        tictactoe_game('HUMAN-HUMAN')
    elif select == str(2):
        tictactoe_game('HUMAN-AI')
    elif select == str(3):
        tictactoe_game('AI-HUMAN')
    elif select == str(4):
        tictactoe_game('AI-AI')
    else:
        main_menu()


if __name__ == '__main__':
    main_menu()