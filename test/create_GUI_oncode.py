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
















# def easy():

#     pass

# def medium():
#     pass

# def difficult():
#     pass





# root = tk()
# root.geometry("850x500")
# root.title("Tic Tac Toe 4*4*4")
# btn1 = Button(root, text="Easy", command=easy,width=15, height=2, font=( 50), fg="black", padx=5, pady=5)
# btn1.pack()
# btn2 = Button(root, text="Medium", command=medium, width=15, height=2, font=(50), bg="black", fg="white", padx=5, pady=5)
# btn2.pack()
# btn3 = Button(root, text="Defficult", command=difficult, width=15, height=2, font=( 50), bg="black", fg="white", padx=5, pady=5)
# btn3.pack()




























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



def ai_move(board, goal, player_turn):
    """This function determines how to move for the AI"""
    if check_if_ai_could_win(board, player_turn) == False:
        if check_if_player_could_win(board, player_turn) == False:
            follow_goal(board, goal, player_turn)

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

def play_tic_tac_toe():
    def on_button_click(b, r, c):
        nonlocal player_turn, turn_count, list_of_goals, goal

        if board[b, r, c] == ' ':
            input_player_move(board, player_turn, (b, r, c))
            button_texts[b, r, c].set(player_turn)

            if check_for_wins(board) != 'None':
                draw_board_label.config(text=draw_board(board))
                messagebox.showinfo("Game Over", f'The winner is {check_for_wins(board)}')
                root.destroy()

            player_turn = swap_player_turn(player_turn)
            turn_count += 1
            while not check_if_goal_valid(goal, board):
                goal = choose_random_goal(list_of_goals)

            draw_board_label.config(text=draw_board(board))
            ai_move(board, goal, player_turn)
            player_turn = swap_player_turn(player_turn)
            turn_count += 1

            if check_for_wins(board) != 'None':
                draw_board_label.config(text=draw_board(board))
                messagebox.showinfo("Game Over", f'The winner is {check_for_wins(board)}')
                root.destroy()

    root = tk.Tk()
    root.title("3D Tic Tac Toe")

    board = np.full((4, 4, 4), ' ')
    player_turn = 'X'
    turn_count = 0
    list_of_goals = create_goals(board)
    goal = choose_random_goal(list_of_goals)

    button_texts = np.empty((4, 4, 4), dtype=tk.StringVar)

    for b in range(4):
        for r in range(4):
            for c in range(4):
                button_texts[b, r, c] = tk.StringVar()
                button_texts[b, r, c].set(board[b, r, c])
                button = tk.Button(root, textvariable=button_texts[b, r, c], font=("Helvetica", 16), width=4, height=2,
                                   command=lambda b=b, r=r, c=c: on_button_click(b, r, c))
                button.grid(row=r, column=c + b * 5)

    draw_board_label = tk.Label(root, text=draw_board(board), font=("Helvetica", 12))
    draw_board_label.grid(row=4, column=0, columnspan=20)


    # def easy():تتتتتتتتتتتتت

    #     pass

    # def medium():
    #     pass

    # def difficult():
    #     pass

    # btn1 = tk.Button(root, text="Easy", command=easy,width=15, height=2, font=( 50), fg="black", padx=5, pady=5)
    # btn1.pack()
    # btn2 = tk.Button(root, text="Medium", command=medium, width=15, height=2, font=(50), bg="black", fg="white", padx=5, pady=5)
    # btn2.pack()
    # btn3 = tk.Button(root, text="Defficult", command=difficult, width=15, height=2, font=( 50), bg="black", fg="white", padx=5, pady=5)
    # btn3.pack()



    root.mainloop()

play_tic_tac_toe()
