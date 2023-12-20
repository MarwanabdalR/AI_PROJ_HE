import numpy as np
import pandas as pd
import random as rnd
import tkinter as tk
from tkinter import messagebox

def draw_board(board):
    """This function print's the game board as panda data frames"""
    frame1 = pd.DataFrame(board[0])
    frame2 = pd.DataFrame(board[1])
    frame3 = pd.DataFrame(board[2])
    frame4 = pd.DataFrame(board[3])

    frame1.index = ['A', 'B', 'C', 'D']
    frame2.index = ['E', 'F', 'G', 'H']
    frame3.index = ['I', 'J', 'K', 'L']
    frame4.index = ['M', 'N', 'O', 'P']

    return f"{frame1}\n\n{frame2}\n\n{frame3}\n\n{frame4}"



def swap_player_turn(player_turn):
    if player_turn == 'X':
        return 'O'
    elif player_turn == 'O':
        return 'X'

def input_player_move(board, player_turn, move):
    b, r, c = move
    board[b, r, c] = player_turn

def check_for_wins(board):
    # Check Layers (horizontal, vertical, and diagonal within a single layer)
    for b in range(4):
        # Check horizontal and vertical layers
        for i in range(4):
            # Horizontal layer
            if all(mark == 'X' for mark in board[b, i, :]) or all(mark == 'O' for mark in board[b, i, :]):
                return board[b, i, 0]
            # Vertical layer
            if all(mark == 'X' for mark in board[b, :, i]) or all(mark == 'O' for mark in board[b, :, i]):
                return board[b, 0, i]
        # Check diagonals within a single layer
        if all(board[b, i, j] == 'X' for j in range(4) for i in range(4)) or all(board[b, i, j] == 'O' for j in range(4) for i in range(4)):
            return board[b, 0, 0]
        if all(board[b, i, 3 - i] == 'X' for i in range(4)) or all(board[b, i, 3 - i] == 'O' for i in range(4)):
            return board[b, 0, 3]

    # Check Rows (horizontal, vertical, and diagonal rows spanning across all layers)
    for i in range(4):
        # Horizontal row
        if all(board[j, i, k] == 'X' for j in range(4) for k in range(4)) or all(board[j, i, k] == 'O' for j in range(4) for k in range(4)):
            return board[0, i, 0]
        # Vertical row
        if all(board[j, k, i] == 'X' for j in range(4) for k in range(4)) or all(board[j, k, i] == 'O' for j in range(4) for k in range(4)):
            return board[0, 0, i]
        # Diagonal row
        if all(board[j, j, i] == 'X' for j in range(4)) or all(board[j, j, i] == 'O' for j in range(4)):
            return board[0, 0, i]
        if all(board[j, 3 - j, i] == 'X' for j in range(4)) or all(board[j, 3 - j, i] == 'O' for j in range(4)):
            return board[0, 3, i]

    # Check Columns (horizontal, vertical, and diagonal columns spanning across all layers)
    for i in range(4):
        # Horizontal column
        if all(board[i, j, k] == 'X' for j in range(4) for k in range(4)) or all(board[i, j, k] == 'O' for j in range(4) for k in range(4)):
            return board[i, 0, 0]
        # Vertical column
        if all(board[j, i, k] == 'X' for j in range(4) for k in range(4)) or all(board[j, i, k] == 'O' for j in range(4) for k in range(4)):
            return board[0, i, 0]
        # Diagonal column
        if all(board[j, k, i] == 'X' for j in range(4) for k in range(4)) or all(board[j, k, i] == 'O' for j in range(4) for k in range(4)):
            return board[0, 0, i]

    # Check Diagonals (connecting different layers)
    for j in range(4):
        # Diagonal connecting different layers
        if all(board[i, j, i] == 'X' for i in range(4)) or all(board[i, j, i] == 'O' for i in range(4)):
            return board[0, j, 0]
        if all(board[i, j, 3 - i] == 'X' for i in range(4)) or all(board[i, j, 3 - i] == 'O' for i in range(4)):
            return board[0, j, 3]

    return 'None'



def ai_move(board, player_turn):
    best_score = float('-inf')
    best_move = None
    goals = create_goals(board)

    for move in goals:
        if check_if_goal_valid([move], board):
            board_copy = board.copy()
            input_player_move(board_copy, player_turn, move)
            score = minimax(board_copy, 0, False)
            if score > best_score:
                best_score = score
                best_move = move

    if best_move is not None:
        input_player_move(board, player_turn, best_move)


def minimax(board, depth, is_maximizing):
    if check_for_wins(board) == 'X':
        return -1
    elif check_for_wins(board) == 'O':
        return 1
    elif depth == 4 * 4 * 4:
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for move in create_goals(board):
            if check_if_goal_valid([move], board):
                board_copy = board.copy()
                input_player_move(board_copy, 'O', move)
                score = minimax(board_copy, depth + 1, False)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in create_goals(board):
            if check_if_goal_valid([move], board):
                board_copy = board.copy()
                input_player_move(board_copy, 'X', move)
                score = minimax(board_copy, depth + 1, True)
                best_score = min(score, best_score)
        return best_score




def choose_random_goal(list_of_goals):
    """Return a random goal, and delete the goal from list of goals"""
    num = rnd.randrange(0, len(list_of_goals))
    goal = list_of_goals[num]
    list_of_goals.pop(num)
    return goal

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


def check_if_goal_valid(goal, board):
    for b, r, c in goal:
        if board[b, r, c] != ' ':
            return False
    return True

# def play_tic_tac_toe():
#     def on_button_click(b, r, c):
#         nonlocal player_turn, turn_count, list_of_goals, goal

#         if board[b, r, c] == ' ':
#             input_player_move(board, player_turn, (b, r, c))
#             button_texts[b, r, c].set(player_turn)

#             if check_for_wins(board) != 'None':
#                 draw_board_label.config(text=draw_board(board))
#                 messagebox.showinfo("Game Over", f'The winner is {check_for_wins(board)}')
#                 root.destroy()

#             player_turn = swap_player_turn(player_turn)
#             turn_count += 1
#             while not check_if_goal_valid(goal, board):
#                 goal = choose_random_goal(list_of_goals)

#             draw_board_label.config(text=draw_board(board))
#             ai_move(board, goal, player_turn)
#         while turn_count < 64 and check_for_wins(board) == 'None':
#             # User's turn
#             if player_turn == 'X':
#                 root.update()
#                 root.update_idletasks()
#             # AI's turn
#             else:
#                 goal = choose_random_goal(list_of_goals)
#                 while not check_if_goal_valid(goal, board, for_user=False):
#                     goal = choose_random_goal(list_of_goals)
#                 ai_move(board, player_turn)
#                 draw_board_label.config(text=draw_board(board))


#             player_turn = swap_player_turn(player_turn)
#             turn_count += 1

#             if check_for_wins(board) != 'None':
#                 draw_board_label.config(text=draw_board(board))
#                 messagebox.showinfo("Game Over", f'The winner is {check_for_wins(board)}')
#             else:
#                 messagebox.showinfo("Game Over", "It's a draw!")

#             root.destroy()

    

#     root = tk.Tk()
#     root.title("3D Tic Tac Toe")

#     board = np.full((4, 4, 4), ' ')
#     player_turn = 'X'
#     turn_count = 0
#     list_of_goals = create_goals(board)
#     goal = choose_random_goal(list_of_goals)

#     button_texts = np.empty((4, 4, 4), dtype=tk.StringVar)

#     for r in range(4):
#         for c in range(4):
#             for b in range(4):
#                 button_texts[b, r, c] = tk.StringVar()
#                 button_texts[b, r, c].set(board[b, r, c])
#                 button = tk.Button(root, textvariable=button_texts[b, r, c], font=("Helvetica", 16), width=4, height=2,
#                                 command=lambda b=b, r=r, c=c: on_button_click(b, r, c))
#                 button.grid(row=r, column=c + b * 5)


#     draw_board_label = tk.Label(root, text=draw_board(board), font=("Helvetica", 12))
#     draw_board_label.grid(row=4, column=0, columnspan=20)














def play_tic_tac_toe():
    root = tk.Tk()
    root.title("3D Tic Tac Toe")

    board = np.full((4, 4, 4), ' ')
    player_turn = 'X'
    turn_count = 0
    list_of_goals = create_goals(board)
    goal = choose_random_goal(list_of_goals)

    button_texts = np.empty((4, 4, 4), dtype=tk.StringVar)

    for r in range(4):
        for c in range(4):
            for b in range(4):
                button_texts[b, r, c] = tk.StringVar()
                button_texts[b, r, c].set(board[b, r, c])
                button = tk.Button(root, textvariable=button_texts[b, r, c], font=("Helvetica", 16), width=4, height=2,
                                   state=tk.DISABLED)  # Disable buttons
                button.grid(row=r, column=c + b * 5)

    draw_board_label = tk.Label(root, text=draw_board(board), font=("Helvetica", 12))
    draw_board_label.grid(row=4, column=0, columnspan=20)

    # Auto-play loop
    while check_for_wins(board) == 'None' and turn_count < 64:  # Continue until someone wins or it's a draw
        root.update_idletasks()
        root.update()

        # Player X move (user input)
        if player_turn == 'X':
            # Add your existing user input code here
            pass

        # Player O move (AI)
        elif player_turn == 'O':
            ai_move(board, goal, player_turn)
            player_turn = swap_player_turn(player_turn)
            turn_count += 1

            # Update the GUI
            draw_board_label.config(text=draw_board(board))
            root.update_idletasks()
            root.update()

            # Delay for better visualization (you can adjust the sleep time)
            time.sleep(1)

    # Game Over
    if check_for_wins(board) != 'None':
        messagebox.showinfo("Game Over", f'The winner is {check_for_wins(board)}')
    else:
        messagebox.showinfo("Game Over", "It's a draw!")

    root.destroy()

# Call the play_tic_tac_toe function to start the game
# play_tic_tac_toe()






















    root.mainloop()

play_tic_tac_toe()
