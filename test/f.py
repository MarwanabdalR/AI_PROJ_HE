import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox

def draw_board(board):
    """This function print's the game board as panda data frames"""
    frames = [pd.DataFrame(layer) for layer in board]
    for i, frame in enumerate(frames):
        frame.index = [f'{row}{i+1}' for row in ['A', 'B', 'C', 'D']]
    return '\n\n'.join(frame.to_string() for frame in frames)


def swap_player_turn(player_turn):
    if player_turn == 'X':
        return 'O'
    elif player_turn == 'O':
        return 'X'

def input_player_move(board, player_turn, move):
    b, r, c = move
    board[b, r, c] = player_turn

def check_for_wins(board):
    # ... (same as before)
    
    """This function returns an 'X' if X has won or an 'O' if O has won."""
    # Check Rows On each board:
    for b in board:
        for row in b:
            countO = 0
            countX = 0
            for column in row:
                if column == 'X':
                    countX += 1
                elif column == 'O':
                    countO += 1
            if countO == 4:
                return 'O'
            if countX == 4:
                return 'X'
    # Check Columns on each board:
    for b in board:
        for row in b.T:
            countX = 0
            countO = 0
            for column in row:
                if column == 'X':
                    countX += 1
                elif column == 'O':
                    countO += 1
            if countX == 4:
                return 'X'
            elif countO == 4:
                return 'O'
    # Check for diaganols on each board:
    for b in board:
        countX = 0
        countO = 0
        for i in range(4):
            if b[i, i] == 'X':
                countX += 1
            elif b[i, i] == 'O':
                countO += 1  
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
        
        countX = 0
        countO = 0
        for x, y in zip(range(3, -1, -1), range(4)):
            if b[x, y] == 'X':
                countX += 1
            elif b[x, y] == 'O':
                countO += 1
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
    # Check for line through board (3d row or column):
    for x in range(4):
        for y in range(4):
            countX = 0
            countO = 0
            for b in board:
                if b[x, y] == 'X':
                    countX += 1
                elif b[x, y] == 'O':
                    countO += 1
            if countX == 4:
                return 'X'
            elif countO == 4:
                return 'O'
    # Check for vertical through board daiaganols:
    for c in range(4):
        countO = 0
        countX = 0
        for r, b in zip(range(4), board):
            if b[r, c] == 'X':
                countX += 1
            elif b[r, c] == 'O':
                countO += 1
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
    for c in range(4):
        countO = 0
        countX = 0
        for r, b in zip(range(3, -1, -1), board):
            if b[r, c] == 'X':
                countX += 1
            elif b[r, c] == 'O':
                countO += 1
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
    # Check for horizontal through board diaganols:
    for r in range(4):
        countX = 0
        countO = 0
        for c, b in zip(range(4), board):
            if b[r, c] == 'X':
                countX += 1
            elif b[r, c] == 'O':
                countO += 1
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
    for r in range(4):
        countX = 0
        countO = 0
        for c, b in zip(range(3, -1, -1), board):
            if b[r, c] == 'X':
                countX += 1
            elif b[r, c] == 'O':
                countO += 1
        if countX == 4:
            return 'X'
        elif countO == 4:
            return 'O'
    # Check for corner to corner diaganols
    countX = 0
    countO = 0
    for r, c, b in zip(range(4), range(4), board):
        if b[r, c] == 'X':
            countX += 1
        elif b[r, c] == 'O':
            countO += 1
    if countX == 4:
        return 'X'
    elif countO == 4:
        return 'O'
    countX = 0
    countO = 0
    for r, c, b in zip(range(4), range(3, -1, -1), board):
        if b[r, c] == 'X':
            countX += 1
        elif b[r, c] == 'O':
            countO += 1
    if countX == 4:
        return 'X'
    elif countO == 4:
        return 'O'
    countX = 0
    countO = 0
    for r, c, b in zip(range(3, -1, -1), range(4), board):
        if b[r, c] == 'X':
            countX += 1
        elif b[r, c] == 'O':
            countO += 1
    if countX == 4:
        return 'X'
    elif countO == 4:
        return 'O'
    countX = 0
    countO = 0
    for r, c, b in zip(range(3, -1, -1), range(3, -1, -1), board):
        if b[r, c] == 'X':
            countX += 1
        elif b[r, c] == 'O':
            countO += 1
    if countX == 4:
        return 'X'
    elif countO == 4:
        return 'O'
    
    return 'None'



def minimax(board, depth, maximizing_player, alpha, beta, player_turn):
    """
    Minimax algorithm with alpha-beta pruning for 4x4x4 Tic-Tac-Toe.
    """
    if depth == 0 or is_board_full(board):
        return evaluate(board, player_turn)

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_valid_moves(board):
            board_copy = board.copy()
            make_move(board_copy, move, player_turn)
            eval = minimax(board_copy, depth - 1, False, alpha, beta, player_turn)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_valid_moves(board):
            board_copy = board.copy()
            make_move(board_copy, move, swap_player_turn(player_turn))
            eval = minimax(board_copy, depth - 1, True, alpha, beta, player_turn)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval




def choose_best_move(board, player_turn):
    """
    Choose the best move for the AI using Minimax algorithm.
    """
    best_eval = float('-inf')
    best_move = None

    for move in get_valid_moves(board):
        board_copy = board.copy()
        make_move(board_copy, move, player_turn)
        eval = minimax(board_copy, depth=3, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), player_turn=player_turn)

        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move



def get_valid_moves(board):
    """
    Get a list of valid moves on the current board.
    """
    return list(zip(*np.where(board == ' ')))



def make_move(board, move, player_turn):
    """
    Make a move on the board for the given player.
    """
    b, r, c = move
    board[b, r, c] = player_turn



def swap_player_turn(player_turn):
    """
    Swap the player turn.
    """
    return 'O' if player_turn == 'X' else 'X'


def ai_move(board, player_turn):
    global list_of_goals

    if check_if_ai_could_win(board, player_turn):
        return  # AI will win on the next move, no need for Minimax

    if check_if_player_could_win(board, player_turn):
        return  # Player can win on the next move, no need for Minimax

    best_eval = float('-inf')
    best_move = None

    for goal in list_of_goals:
        if check_if_goal_valid(goal, board):
            board_copy = board.copy()
            for move in goal:
                b, r, c = move
                board_copy[b, r, c] = player_turn

            eval = minimax(board_copy, depth=3, maximizing_player=False, alpha=float('-inf'), beta=float('inf'), player_turn=player_turn)

            if eval > best_eval:
                best_eval = eval
                best_move = goal

    if best_move:
        for move in best_move:
            b, r, c = move
            input_player_move(board, player_turn, (b, r, c))




def evaluate(board, player_turn):
    """
    Evaluate the current state of the board for the given player.
    """
    # Check for wins on layers
    for layer in board:
        if np.any(np.all(layer == player_turn, axis=0)):
            return 1

    # Check for wins on rows
    if np.any(np.all(board == player_turn, axis=(1, 2))):
        return 1

    # Check for wins on columns
    if np.any(np.all(board == player_turn, axis=(0, 2))):
        return 1

    # Check for wins on diagonals
    if np.any(np.all(board == player_turn, axis=(0, 1))):
        return 1

    # Check for wins on cross-diagonals
    if np.all(np.diagonal(board, axis1=0, axis2=1) == player_turn) or np.all(np.diagonal(board[:, ::-1, :], axis1=0, axis2=1) == player_turn):
        return 1

    # Check for wins on cross-rows
    if np.all(np.diagonal(board, axis1=1, axis2=2) == player_turn) or np.all(np.diagonal(board[:, :, ::-1], axis1=1, axis2=2) == player_turn):
        return 1

    # Check for wins on cross-columns
    if np.all(np.diagonal(board, axis1=0, axis2=2) == player_turn) or np.all(np.diagonal(board[:, ::-1, :], axis1=0, axis2=2) == player_turn):
        return 1

    # Check for wins on cross-layers
    if np.all(np.diagonal(board, axis1=0, axis2=1) == player_turn) or np.all(np.diagonal(board[::-1, :, :], axis1=0, axis2=1) == player_turn):
        return 1

    return 0  # No winner yet



list_of_goals = []
def is_board_full(board):
    """
    Check if the board is full, indicating a draw.
    """
    return np.all(board != ' ')























def check_if_player_could_win(board, player_turn):
    # Check for potential wins in rows
    for b in board:
        for row in b:
            count_empty = 0
            count_player = 0
            for column in row:
                if column == ' ':
                    count_empty += 1
                elif column == player_turn:
                    count_player += 1
            if count_empty == 1 and count_player == 3:
                return True

    # Check for potential wins in columns
    for b in board:
        for col in b.T:
            count_empty = 0
            count_player = 0
            for cell in col:
                if cell == ' ':
                    count_empty += 1
                elif cell == player_turn:
                    count_player += 1
            if count_empty == 1 and count_player == 3:
                return True

    # Check for potential wins in diagonals
    for b in board:
        diag1_count_empty = 0
        diag1_count_player = 0
        diag2_count_empty = 0
        diag2_count_player = 0
        for i in range(4):
            if b[i, i] == ' ':
                diag1_count_empty += 1
            elif b[i, i] == player_turn:
                diag1_count_player += 1

            if b[i, 3 - i] == ' ':
                diag2_count_empty += 1
            elif b[i, 3 - i] == player_turn:
                diag2_count_player += 1

        if (diag1_count_empty == 1 and diag1_count_player == 3) or (diag2_count_empty == 1 and diag2_count_player == 3):
            return True

    return False


def check_if_ai_could_win(board, player_turn):
    # Check for potential wins in rows
    for b in board:
        for row in b:
            count_empty = 0
            count_ai = 0
            for column in row:
                if column == ' ':
                    count_empty += 1
                elif column == player_turn:
                    count_ai += 1
            if count_empty == 1 and count_ai == 3:
                return True

    # Check for potential wins in columns
    for b in board:
        for col in b.T:
            count_empty = 0
            count_ai = 0
            for cell in col:
                if cell == ' ':
                    count_empty += 1
                elif cell == player_turn:
                    count_ai += 1
            if count_empty == 1 and count_ai == 3:
                return True

    # Check for potential wins in diagonals
    for b in board:
        diag1_count_empty = 0
        diag1_count_ai = 0
        diag2_count_empty = 0
        diag2_count_ai = 0
        for i in range(4):
            if b[i, i] == ' ':
                diag1_count_empty += 1
            elif b[i, i] == player_turn:
                diag1_count_ai += 1

            if b[i, 3 - i] == ' ':
                diag2_count_empty += 1
            elif b[i, 3 - i] == player_turn:
                diag2_count_ai += 1

        if (diag1_count_empty == 1 and diag1_count_ai == 3) or (diag2_count_empty == 1 and diag2_count_ai == 3):
            return True

    return False









def create_goals(board):
    """This function returns a random goal for the ai"""
    list_of_goals = []

    # Create all possible horizontal lines on each board
    for b_num, b in enumerate(board):
        for r_num, r in enumerate(b):
            row = []
            for c_num, c in enumerate(r):
                row.append((b_num, r_num, c_num))
            list_of_goals.append(row)
    # Create all possible vertical lines on each board
    for b_num, b in enumerate(board):
        for c in range(4):
            column = []
            for r in range(4):
                column.append((b_num, r, c))
            list_of_goals.append(column)
    # Create all possible diaganol lines on each board
    for b in range(4):
        diag = []
        for r, c, in zip(range(4), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    for b in range(4):
        diag = []
        for r, c, in zip(range(3, -1, -1), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    # Create all possible lines through baord
    for r in range(4):
        for c in range(4):
            line = []
            for b in range(4):
                line.append((b, r, c))
            list_of_goals.append(line)
    # Create vertical through board diaganols
    for c in range(4):
        diag = []
        for r, b, in zip(range(4), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    for c in range(4):
        diag = []
        for r, b, in zip(range(3, -1, -1), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    # Create horizontal through board diaganols
    for r in range(4):
        diag = []
        for c, b in zip(range(4), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    for r in range(4):
        diag = []
        for c, b in zip(range(3, -1, -1), range(4)):
            diag.append((b, r, c))
        list_of_goals.append(diag)
    # Create corner to corner through board diaganols:
    diag = []
    for b, r, c in zip(range(4), range(4), range(4)):
        diag.append((b, r, c))
    list_of_goals.append(diag)
    diag = []
    for b, r, c in zip(range(4), range(4), range(3, -1, -1)):
        diag.append((b, r, c))
    list_of_goals.append(diag)
    diag = []
    for b, r, c in zip(range(4), range(3, -1, -1), range(4)):
        diag.append((b, r, c))
    list_of_goals.append(diag)
    diag = []
    for b, r, c in zip(range(4), range(3, -1, -1), range(3, -1, -1)):
        diag.append((b, r, c))
    list_of_goals.append(diag)

    return list_of_goals

list_of_goals = create_goals(np.full((4, 4, 4), ' '))



def check_if_goal_valid(goal, board):
    for b, r, c in goal:
        if board[b, r, c] != ' ':
            return False
    return True










# this multi player
# def play_tic_tac_toe():
#     # global list_of_goals    

#     def on_button_click(b, r, c):
#         nonlocal player_turn, turn_count

#         if board[b, r, c] == ' ':
#             input_player_move(board, player_turn, (b, r, c))
#             button_texts[b, r, c].set(player_turn)

#             if check_for_wins(board) != 'None':
#                 draw_board_label.config(text=draw_board(board))
#                 messagebox.showinfo("Game Over", f'The winner is {check_for_wins(board)}')
#                 root.destroy()

#             player_turn = swap_player_turn(player_turn)
#             turn_count += 1

#             draw_board_label.config(text=draw_board(board))
#             ai_move(board, player_turn)
#             player_turn = swap_player_turn(player_turn)
#             turn_count += 1

#             if check_for_wins(board) != 'None':
#                 draw_board_label.config(text=draw_board(board))
#                 messagebox.showinfo("Game Over", f'The winner is {check_for_wins(board)}')
#                 root.destroy()
#     global list_of_goals
#     root = tk.Tk()
#     root.title("3D Tic Tac Toe")
#     list_of_goals = create_goals(board)

#     board = np.full((4, 4, 4), ' ')
#     player_turn = 'X'
#     turn_count = 0

#     button_texts = np.empty((4, 4, 4), dtype=tk.StringVar)

#     for b in range(4):
#         for r in range(4):
#             for c in range(4):
#                 button_texts[b, r, c] = tk.StringVar()
#                 button_texts[b, r, c].set(board[b, r, c])
#                 if c % 4 == 3:
#                     button = tk.Button(root, textvariable=button_texts[b, r, c], font=("Helvetica", 16), width=4, height=2,
#                                     command=lambda b=b, r=r, c=c: on_button_click(b, r, c))
#                     button.grid(row=r, column=c + b * 5, padx=5)
#                 else:
#                     button = tk.Button(root, textvariable=button_texts[b, r, c], font=("Helvetica", 16), width=4, height=2,
#                                     command=lambda b=b, r=r, c=c: on_button_click(b, r, c))
#                     button.grid(row=r, column=c + b * 5, padx=5)
#     draw_board_label = tk.Label(root, text=draw_board(board), font=("Helvetica", 12))
#     draw_board_label.grid(row=4, column=0, columnspan=20)

#     root.mainloop()

# play_tic_tac_toe()

